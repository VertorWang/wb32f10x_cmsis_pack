# 本仓库用于构建WB32F10x芯片的CMSIS PACK

## 使用方法
1. 在 svd_generate/periph/目录下编写芯片的寄存器定义，之后运行 svd_generate/wb32f10x.py生成xml格式的SVD文件
2. 拷贝生成的 svd_generate/WestBerry.WB32F10x_DFP/SVD/WB32F10x.svd 到 /pack_generate/Files/SVD目录下
3. 修改 /pack_generate/WestBerry.WB32F10x_DFP.pdsc(可以不做)
4. 修改 /pack_generate/Device,/pack_generate/Flash(同第4步)
5. 在命令行运行./gen_pack.bat脚本生成最终的pack