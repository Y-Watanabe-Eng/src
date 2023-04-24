Public Declare Sub Sleep Lib "kernel32" (ByVal dwMilliseconds As Long)

Sub Create_Word()

Dim wordApp As Object
Dim wordDoc As Word.Document
Dim thisYYYYMM As Long
Dim i As Long
Dim name As String
Dim excelText1 As String
Dim excelText2 As String
Dim excelText3 As String



'変数tmに今月、lmに先月の値を取得
Dim tm  As Date: tm = DateSerial(Year(Date), Month(Date), 1)
Dim lm  As Date: lm = DateSerial(Year(Date), Month(Date) - 1, 1)

'年度を取得
Dim fiscalYear As String

If month(Date) <= Then

　fiscalYear = Year(Date) - 1 & "年度"

Else

　fiscalYear = Year(Date) & "年度"

End If


' CreateObject関数でオブジェクトを作成し変数にセット
Set wordApp = CreateObject("Word.Application") 

'Wordを起動する
wordApp.Visible = True

With wordApp



'6行分繰り返す(46行目から51行目まで）
For i = 46 To 51

'指定したWordファイルを起動
Set wordDoc = WordApp.Documents.Open("¥¥csysu01¥共有フォルダ¥6_チェックリスト" & fiscalYear & "¥インシデントチェック改善取り組み（個人）¥【テンプレート】yyyymm_name.docx") 


'1000ミリ秒待機
Sleep 1000


'EXCELのテキストデータを代入
name = ThisWorkbook.Worksheets("分析結果").Cells(i, "A").Value
excelText1 = ThisWorkbook.Worksheets("分析結果").Cells(i, 3).Text
excelText2 = ThisWorkbook.Worksheets("分析結果").Cells(i, 4).Text
excelText3 = ThisWorkbook.Worksheets("分析結果").Cells(i, 5).Text


'代入したテキストデータをWordへ置換
wordDoc.Content.Find.Execute _
        FindText:="@今月@", _
        ReplaceWith:=month(tm) & "月", _
        Replace:=2

wordDoc.Content.Find.Execute _
        FindText:="@先月@", _
        ReplaceWith:=month(lm) & "月", _
        Replace:=2

wordDoc.Content.Find.Execute _
        FindText:="@対応件数@", _
        ReplaceWith:=excelText1, _
        Replace:=1

wordDoc.Content.Find.Execute _
        FindText:="@チェック件数@", _
        ReplaceWith:=excelText2, _
        Replace:=1

wordDoc.Content.Find.Execute _
        FindText:="@チェック率@", _
        ReplaceWith:=excelText3, _
        Replace:=1


'新規フォルダを作成
Dim newFolder As String
newDocPath = "¥¥csysu01¥共有フォルダ¥6_チェックリスト" & fiscalYear & "¥インシデントチェック改善取り組み（個人）¥" & name & "¥1.個人取り組み¥" & Format(Date, ”yyyymm”)


Dim newDocPath As String
newDocPath = "¥¥csysu01¥共有フォルダ¥6_チェックリスト" & fiscalYear & "¥インシデントチェック改善取り組み（個人）¥1.個人取り組み¥" & Format(Date, ”yyyymm”) & "¥" & Format(Date, ”yyyymm”) & "_" & name & ".docx"

wordDoc.SaveAs2 newDocPath

wordDoc.Close savechanges:=False

Next i

End With


'Wordを終了
wordApp.Quit

MsgBox "処理が完了しました。"

End Sub
