# Hamiltonian cycle finder

## Описание

Ищет [Гамильтоновы циклы](https://ru.wikipedia.org/wiki/Гамильтонов_граф "Wikipedia") в графах в формате [Graphoid2021](https://github.com/Anton00756/Graphoid--2021 "Github").

## Использование

```bash
hamiltonian_cycle.exe input.txt
```
Работает с ориентированными и неориентированными графами.
Дополнительные параметры получает через поле `<text>`

```
<text>
color = цвет подсветки цикла (по умолчанию red)
del_ribs = удалять ли рёбра вне цикла? (по умолчанию false)
index = индекс цикла в графе (по умолчанию 0)
clear = очищать ли граф перед поиском цикла? (по умолчанию false)
clear_color = цвет рёбер чистого графа (по умолчанию blue)
```

## Сборка  

```bash
pyinstaller make/make.spec
```