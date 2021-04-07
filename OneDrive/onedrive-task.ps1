# Powershell script to copy Enishi job schedule worksheet to OneDrive
# スタジオ縁の予定表（エクセル）をOneDriveへコピーする。
# 2020/09 H. Gonzalez
#
# 注意！！　このスクリプトはPC08から実行するに開発された。他のパソコンから実行の場合、ソースをチェック下さい。
#
$LOGFILE = "C:\Users\PC08\OneDrive\ドキュメント\sync-history.txt"
# $SOURCEDIR = "Z:\★第８期\"
# $SOURCEFNAME = "第８期　作業予定表（Ｒ2.4.1～Ｒ3.3.31）.xlsx"
$SOURCEDIR = "Z:\★第９期\"
$SOURCEFNAME = "９期作業予定表.xlsx"
$SOURCEFILE = $SOURCEDIR + $SOURCEFNAME
$DESTDIR = "C:\Users\PC08\OneDrive\"
$DESTFILE = $DESTDIR + $SOURCEFNAME
$EASYFILE = $DESTDIR + "見やすい予定表.xlsx"
Get-Date -Format "yyyy-MM-dd HH:mm:ss" >> $LOGFILE

# Compare dates and abort if source file hasn't changed
$dateA = (Get-Item $SOURCEFILE ).LastWriteTime
$dateB = Get-Date -Year 2000 -Month 01 -Day 01      # initialize to an old date to ensure copy happens even if file doesn't exist
if ([System.IO.File]::Exists($DESTFILE)) {
    $dateB = (Get-Item $DESTFILE).LastWriteTime
}
if ($dateA -gt $dateB) {
    Copy-Item $SOURCEFILE -Destination $DESTFILE -Verbose   *>> $LOGFILE
    Copy-Item $SOURCEFILE -Destination $EASYFILE -Verbose

    # do some excel VBA magic
    "Launching Excel VBA Script." *>> $LOGFILE
    $excel = New-Object -ComObject excel.application
    $workbook = $excel.workbooks.open("Z:\〇事務仕事〇\OneDrive\tools.xlsm")
    $excel.Run("OpenSched", $EASYFILE)
    $workbook.close()
    $excel.quit()
} else {
    "Source file is unmodified, skipping." >> $LOGFILE
}

Write-Output "" >> $LOGFILE
