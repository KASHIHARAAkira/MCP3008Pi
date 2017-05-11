>日本語は下にあります。
# MCP3008 with Raspberry Pi
## Introduction
  This module provide some method using MCP3008. If you want to use this module, you have to enable SPI on your Raspberry Pi and install spi-dev. This README tell you how to do them.
  I assume that you use Raspbian on your Raspberry Pi.

## Usage
### Sample Code
```
#!/usr/bin/env python

from MCP3008Pi import mcp3008

mcp = mcp3008.MCP3008(0,0)

print(mcp.read(0))

mcp.close()
```

## Install Relational Packege
### Enable SPI on Your Raspberry Pi
  You run the following script on terminal. This process need about  20-30 minitus.

```
sudo apt-get update
sudo apt-get upgrade
sudo rpi-update
```

  You choose Menu=>Preference=>Raspberry Pi Configuration=>Interface=>SPI and select enable.
  Then you reboot your raspberry Pi

### Install spidev
  You run the following script on your terminal.

```
cd ~
git clone git://github.com/doceme/py-spidev
cd py-spidev
sudo python setup.py install
```

## Confirm spi

```
python
import spidev
```
If you not get some error, sucess install spidev.

## LICENCE
  This module is provided under MIT Licence. The detail of it is on LICENCE file.

## Bugs
  If you find some bugs of this module, please create new issues on the folloing.

  https://github.com/KASHIHARAAkira/MCP3008Pi/issues

> ここから日本語
## 概要
  　このモジュールはMCP3008を使ってアナログ・デジタル変換を行った値を取ってくるためのモジュールです。もしも、本モジュールを使う場合はお使いのRaspberry PiのSPIを有効にする必要があります
  これらの操作に関しても、このREADMEで記載します。
  　このモジュールはRaspbianでの動作を想定しています。

## 使用方法
### サンプルコード
```
#!/usr/bin/env python

from MCP3008Pi import mcp3008

mcp = mcp3008.MCP3008(0,0)

print(mcp.read(0))

mcp.close()
```

## 関連するパッケージのインストール
### Raspberry PiのSPIを有効にする
  以下のコマンドをterminalで実行してください。20-30分ほどかかります。

```
sudo apt-get update
sudo apt-get upgrade
sudo rpi-update
```

　上のコマンドの処理が終わったらMenu=>Preference=>Raspberry Pi Configuration=>Interface=>SPIを選択し、SPIのところを"enable"に変更します。その後再起動してください。

### spidevのインストール
  以下のコマンドをterminalで実行してください。

```
cd ~
git clone git://github.com/doceme/py-spidev
cd py-spidev
sudo python setup.py install
```

## SPIが使用できるか確認
以下のコマンドを実行して、エラーが出なければspidevのinstallに成功しています。

```
python
import spidev
```

## ライセンス
　このモジュールは、MIT Licenceの下で提供されています。詳しくはLICENCEファイルを御覧ください。

## Bugs
  もしも本モジュールのバグを見つけられた方は、以下のサイトでissueの発行をお願い致します。

  https://github.com/KASHIHARAAkira/MCP3008Pi/issues

