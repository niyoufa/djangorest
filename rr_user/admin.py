#coding: utf-8

from django import forms
from django.contrib import admin
from django.contrib.auth.models import Group as DjangoGroup
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
import json
from rr_user.models import User

# 新增用户表单
class UserCreateForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    username = forms.RegexField(label="Username", max_length=30,
        regex=r'^[\w.@+-]+$',
        help_text=("Required. 30 characters or fewer. Letters, digits and "
                    "@/./+/-/_ only."),
        error_messages={
            'invalid': ("This value may contain only letters, numbers and "
                         "@/./+/-/_ characters.")})
    type = forms.RegexField(label="Type", max_length=10,
        regex=r'^[\w.@+-]+$',
        help_text=("Required. 30 characters or fewer. Letters, digits and "
                    "@/./+/-/_ only."),
        error_messages={
            'invalid': ("This value may contain only letters, numbers and "
                         "@/./+/-/_ characters.")})
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(
        label='Password confirmation',
        widget=forms.PasswordInput,
    )

    class Meta:
        model = User
        fields = ('username', 'type')
        
    def clean_type(self):
        # Since User.username is unique, this check is redundant,
        # but it sets a nicer error message than the ORM. See #13147.
        username = self.cleaned_data["username"]
        type = self.cleaned_data.get("type")
        try:
            User.objects.get(username=username,type=type)
        except User.DoesNotExist:
            return type
        raise forms.ValidationError(u'该用户已存在')

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(json.dumps(self.cleaned_data))
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(UserCreateForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

# 修改用户表单
class UserChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = '__all__'
        
    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]

# 注册用户
class MyUserAdmin(UserAdmin):

    form = UserChangeForm
    add_form = UserCreateForm

    list_display = ('username', 'createTime', 'nickname', 'name', 'sex', 'email', 'type')
    search_fields = ('username', 'email')
    list_filter = ('type',)
    readonly_fields = ('createTime', 'modifyTime')
    fieldsets = (
        (None, {'fields': ('username', 'email', 'password',)}),
        ('Personal info', {'fields': ('createTime', 'modifyTime')}),
        ('Important dates', {'fields': ('last_login',)}),
    )
    add_fieldsets = (
        (
            None,
            {
                'classes': ('wide',),
                'fields': ('username', 'nickname', 'name', 'sex', 'email', 'password1', 'password2', 'type'),
            }
        ),
    )
    ordering = ('createTime',)
    filter_horizontal = ()


admin.site.register(User, MyUserAdmin)