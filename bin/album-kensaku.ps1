# Search for album names in Dexpert album definition (.kad) files using Get-ChildItem.
# H.Gonzalez 2020-12-14
#
"デキスパート　写管屋アルバム　検索　ツール　【㈱スタジオ縁 2020-12】"
""
"共有にあるデキスパートデータ　アルバム名を探す道具です。"
"アルバム名　か　アルバム名の部分　検索します。"
"例："
"　　　 八木が谷"
"　　　 44-057     （半角／全角に注意）"
""

# Prompt for search string
$needle = Read-Host "検索"
"検索中..."

# Search in current items
gci -Path 'Z:\デキスパートDATA\' -Recurse -Depth 5 -Filter *$needle*.kad 

Read-Host "ENTERキーで終了"
