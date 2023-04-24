Sub Beginning()

'年度を取得
Dim fiscalYear As String

If Month(Date)  <= 3 Then

　fiscalYear = Year(Date) - 1

Else

　fiscalYear = Year(Date) 

End If

CreateObject("WScript.Shell").Run "C:¥Users¥Test¥Desktop¥Sample1.lnk"

CreateObject("WScript.Shell").Run "C:¥Users¥Test¥Desktop¥Sample2.url"

CreateObject("WScript.Shell").Run "C:¥Users¥Test¥Desktop¥Sample3.lnk"

CreateObject("WScript.Shell").Run "C:¥Users¥Test¥Desktop¥Sample4.lnk"


Dim wordApp As Object
Dim wordDoc As Word.Document


' CreateObject関数でオブジェクトを作成し変数にセット
Set wordApp = CreateObject("Word.Application") 

'Wordを起動する
wordApp.Visible = True

Set wordDoc = wordApp.Documents.Open("C:¥Users¥Test¥Desktop¥テンプレート.docx")

Workbooks.Open "¥¥csysu01¥共有フォルダ¥6_チェックリスト¥" & fiscalYear & "¥インシデントチェック表" & Format(DateAdd("m", 0, Date), "yyyymm") & ".xlsx"

End Sub
