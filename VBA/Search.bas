Sub CommandButton1_Click()
'検索ボタン

Dim Target As String
Target = TextBox1.Text

'テキストボックスの入力内容でA列を検索
　ActiveSheet.Range("A9").AutoFilter _
　　Field:=1,  _
　　　Criteria1:="=*" & Target & "*"

End Sub



Sub CommandButton2_Click()
'解除ボタン（テキストボックスクリア）

'エラー（オートフィルタ解除状態で実行すると発生）を無視
　On Error Resume Next

'オートフィルタ解除
　ActiveSheet.ShowAllData 

'テキストボックスクリア
　If TextBox1.Text <> "" Then

　　TextBox1.Text = ""

　End If

End Sub



Sub TextBox1_KeyDown(ByVal KeyCode As MSForms.ReturnInteget, ByVal Shift As Integer)
'Enterキーで検索

If KeyCode = 13 Then

　Call CommandButton1_Click

End If

End Sub
