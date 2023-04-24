Sub Copy_List()
'ソートしたリストを別ブックに転記

Dim lastRow As String


'年度を取得
Dim fiscalYear

If Month(Date)  <= 3 Then

　fiscalYear = Year(Date) - 1

Else

　fiscalYear = Year(Date) 

End If

'転記元のブックを取得
Dim baseBook As Workbook

Set baseBook = ActiveWorkbook


'転記先のブックを開く
If Month(Date)  <= 9 Then

　Workbooks.Open "¥¥csysuf01¥共有フォルダ¥4_詳細分析¥" & fiscalYear & "年度¥インシデントチェック詳細分析" & Format(DateAdd("m", 0, Date), "yyyy") & "0" & Worksheets(”インシデントチェック集計”).Range("B1") & .xlsx"

Else

　Workbooks.Open "¥¥csysuf01¥共有フォルダ¥4_詳細分析¥" & fiscalYear & "年度¥インシデントチェック詳細分析" & Format(DateAdd("m", 0, Date), "yyyy") & Worksheets(”インシデントチェック集計”).Range("B1") & .xlsx"

End If


'転記先のブックを取得
Dim updateBook As Workbook

Set updateBook = ActiveWorkbook


'オートフィルタを解除する
　On Error Resume Next

　　baseBook.Worksheets("インシデントチェック後半").ShowAllData

　On Error GoTo 0


　baseBook.Worksheets("インシデントチェック後半").Range("A1").AutoFilter Field:=8, Criteria1:="修正"
　baseBook.Worksheets("インシデントチェック後半").Range("A1").AutoFilter Field:=10, Criteria1:=""


　lastRow = baseBook.Worksheets("インシデントチェック後半").Cells(Rows.Count, 1).End(xlUp).Row


　baseBook.Worksheets("インシデントチェック後半").Rows("2:" & lastRow).Copy _
　　Dastination:=updateBook.Worksheets("インシデントチェック後半").Rows(2)

　updateBook.Close SaveChanges:=True

End Sub
