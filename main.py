import flet as ft

def main(page: ft.Page):
    page.title = "تطبيق Flet بسيط"
    
    def show_notification(e):
        # اظهار الإشعار
        text = input_field.value
        page.snack_bar = ft.SnackBar(ft.Text(text))
        page.snack_bar.open = True
        page.update()

    # إنشاء حقل الإدخال
    input_field = ft.TextField(label="أدخل نصا هنا", width=300)
    
    # إنشاء زر
    submit_button = ft.ElevatedButton(text="عرض الإشعار", on_click=show_notification)
    
    # إضافة العناصر إلى الصفحة
    page.add(input_field, submit_button)
    page.update()

# تشغيل التطبيق
ft.app(target=main)
