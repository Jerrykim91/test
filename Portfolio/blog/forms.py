from django import forms


class PostSearchForm(forms.Form):
    search_word = forms.CharField(label='Search Word')


# class BlogForm(forms.ModelForm):  # 모델폼 상속
#     class Meta:
#         widgets = {  # 이 속성의 추가로 입력항목에 부트스트랩의 클래스를 추가해 넣을 수 있다.
#             'title': forms.TextInput(attrs={'class': 'form-control'}),
#             'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 10}),
#         }

#         labels = {  # 이 속성의 추가로 나타내는 내용을 표시할 수 있음.
#             'subject': '제목',
#                     'content': '내용',
#         }
