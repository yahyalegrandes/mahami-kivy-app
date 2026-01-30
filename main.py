from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput


class MahamiApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)

        title = Label(
            text="تطبيق مهامي",
            font_size=24,
            size_hint=(1, 0.2)
        )

        self.task_input = TextInput(
            hint_text="اكتب مهمة جديدة",
            size_hint=(1, 0.2)
        )

        add_button = Button(
            text="إضافة المهمة",
            size_hint=(1, 0.2)
        )
        add_button.bind(on_press=self.add_task)

        self.tasks_label = Label(
            text="",
            size_hint=(1, 0.4)
        )

        layout.add_widget(title)
        layout.add_widget(self.task_input)
        layout.add_widget(add_button)
        layout.add_widget(self.tasks_label)

        return layout

    def add_task(self, instance):
        task = self.task_input.text.strip()
        if task:
            self.tasks_label.text += f"- {task}\n"
            self.task_input.text = ""


if __name__ == "__main__":
    MahamiApp().run()
