# flutter-python-asset-maker
generate  flutter asset 


## usage

download python and yml to your project rootdir

run the py
```
python3 assets_maker.py
```

then, generate a yml and dart file

## tip

The generated files do not contain annotations of the source YML files, and the order will turn into alphabetical order, so you can copy the asset related code yourself to your pubspec.yml, and the default file is pub.yaml. if you don't care about these, you can modify the config file.


## 中文说明
下载yml文件,python文件到你的项目根目录

在命令行执行`python3 assets_maker.py`,我这里是mac
你可能需要自己安装python环境

## 说明
默认生成的文件不带注释,且会按照字母顺序排序,所以我这里不会覆盖源配置文件,如果你不在乎顺序,也不在乎原来的配置文件中的注释,也可以自己修改配置文件
