(src|href)="((img|css|js).\*?)"
$1 = "{% static '$2'%}"
