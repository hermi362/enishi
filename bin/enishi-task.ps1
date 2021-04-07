
$excel = new-object -comobject excel.application
$workbook = $excel.workbooks.open("Z:\事務仕事\OneDrive\tools.xlsm")
$worksheet = $workbook.worksheets.item(1)
$excel.Run("Test2")
# $workbook.save()
# $workbook.close()
$excel.quit()

