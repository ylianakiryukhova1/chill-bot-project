# kivi-project
kivi report &amp; telegram chat-bot 


гугл-док с полезными ссылками https://docs.google.com/document/d/1117uHtMYb4tTymRLNbWzcdxaAkiTvaClOdpgfpSXxzw/edit
ссылка на скачивание kivy - https://kivy.org/doc/stable/gettingstarted/installation.html


Наконец, установите Kivy, используя один из следующих вариантов:

Предварительно скомпилированные диски ¶
Самый простой - установить текущую стабильную версию kivyи, kivy_examples при желании, предоставленную командой kivy колеса PyPi. Просто сделайте:

python -m pip install kivy[base] kivy_examples
Это также устанавливает минимальные зависимости Kivy. Чтобы дополнительно установить Kivy с поддержкой аудио / видео , установите либо kivy[base,media]или kivy[full].
Чтобы установить стабильную версию Kivy, в терминале выполните:

python -m pip install kivy[base] kivy_examples --no-binary kivy
Чтобы установить последнюю передовую версию Kivy от мастера , выполните следующие действия:

python -m pip install "kivy[base] @ https://github.com/kivy/kivy/archive/master.zip"
Установка с помощью Conda ¶
Если вы используете Anaconda , вы можете установить Kivy с его менеджером пакетов Conda, используя:

conda install kivy -c conda-forge
Не используйте pip для установки kivy, если вы используете Anaconda, если вы не устанавливаете из исходников.
