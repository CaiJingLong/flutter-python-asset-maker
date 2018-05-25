import os

import yaml

pub_file = open('pubspec.yaml')
pub_yml = yaml.load(pub_file)

assets = pub_yml.get('flutter').get('assets')
haveAssets = assets is not None

config_file = open('assets_maker_config.yml')
config_yaml = yaml.load(config_file)
scan_path = config_yaml.get('image')

if not os.path.isdir(scan_path):
    print(scan_path + "is not a path")
    exit()

print("config finish... wait for make file")

files = os.listdir(scan_path)

d: dict = pub_yml.get('flutter')

# if haveAssets:
#     d: dict = type(pub_yml.get('flutter'))
#     d["assets"] = None

asset_list = []
for f in files:
    asset_list.append("%s/%s" % (scan_path, f))

d["assets"] = asset_list

filename = config_yaml.get('outputfilename')

if filename is None:
    filename = "pub.yaml"

yaml.dump(pub_yml, open('pub.yaml', mode='w'), default_flow_style=False, )

print("""build a file from your image ,file name is %s,remove all comment and sort,
you need copy you need code,
""" % filename)

dartname = config_yaml.get('dartfilename')
if dartname is None:
    filename = "MyAssert.dart"

static = ""
tab = "    "

for f in files:
    f: str = f
    index = f.rfind(".")
    field_name = f[:index].upper()
    static += '%sstatic const String %s = "%s/%s";\n\n' % (tab, field_name, scan_path, f)

dart = """
class MyAssets{

%s
}
""" % static

with(open("./lib/%s" % dartname, mode='w')) as f:
    f.write(dart)

print("build dart file %s,have assert" % dartname)
