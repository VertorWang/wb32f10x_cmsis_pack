# 删除中间文件
rm .\scripts\svd_generate\WestBerry.WB32F10x_DFP\SVD\*.txt
rm .\scripts\svd_generate\WestBerry.WB32F10x_DFP\SVD\*.h
rm .\scripts\svd_generate\WestBerry.WB32F10x_DFP\SVD\*.svd
rm .\WestBerry.WB32F10x_DFP\Files\SVD\*
rm .\WestBerry.WB32F10x_DFP\*.pack
rm .\*.pack

# 进入svd_generate目录下,生成svd文件
Set-Location .\scripts\svd_generate
python.exe .\wb32f10x.py
# 回到根目录
Set-Location ..\..\

# 进入svd目录下,使用SVDConv.exe检查svd文件，将输出的log保存到根目录下
Set-Location .\scripts\svd_generate\WestBerry.WB32F10x_DFP\SVD\
.\SVDConv.exe .\WB32F10x.svd > ../../../../SVDCheck.log

# 回到根目录
Set-Location ..\..\..\..\

# 拷贝.svd到Files中
cp .\scripts\svd_generate\WestBerry.WB32F10x_DFP\SVD\WB32F10x.svd .\WestBerry.WB32F10x_DFP\Files\SVD/WB32F10x.svd

# 进入WestBerry.WB32F10x_DFP目录中
Set-Location .\WestBerry.WB32F10x_DFP\
# 生成pack
.\gen_pack.bat

# 回到根目录
Set-Location ..\
# 移动pack到根目录
mv .\WestBerry.WB32F10x_DFP\*.pack .\