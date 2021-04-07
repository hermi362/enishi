# Search for project names in Dexpert project description (.koj) files using recursive grep and display the file path of any search hits.
# H.Gonzalez 2020-11-25
#
# The motivation for this utility comes from the inability to easily find a Dexpert project's folder when all you know is the project's name.
# H.Gonzalez 2020-12
#
"デキスパート工事　検索　ツール　【㈱スタジオ縁 2020-11】"
""
"サーバーの共有にあるデキスパート工事を探す道具です。"
"工事名　か　工事名の部分　検索します。"
"例："
"　　　 小仲台"
"　　　 03-095     （半角に注意）"
""

# Prompt for search string
$needle = Read-Host "検索"

# Search in current items
gci -Path 'Z:\デキスパートDATA\' -Recurse -Depth 2 -Filter *.koj | Select-String  -Encoding 'OEM' -Pattern $needle 
# Search in deleted items
gci -Path 'Z:\デキスパートDATA\' -Recurse -Depth 2 -Filter *.dst | Select-String  -Encoding 'OEM' -Pattern $needle 

Read-Host "ENTERキーで終了"
