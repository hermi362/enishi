$excel = New-Object -ComObject excel.application
$workbook = $excel.workbooks.open("Z:\事務仕事\OneDrive\tools.xlsm")
$excel.Run("OpenSched", "C:\Users\PC08\OneDrive\ドキュメント", "y8test.xlsx")
$workbook.close()
$excel.quit()
