# Hamiltonian cycle finder

## Описание

Ищет [Гамильтоновы циклы](https://ru.wikipedia.org/wiki/Гамильтонов_граф "Wikipedia") в графах в формате [Graphoid2021](https://github.com/Anton00756/Graphoid--2021 "Github").

## Использование

```bash
hamiltonian_cycle.exe input.txt
```
Работает с ориентированными и неориентированными обыными графами.
Дополнительные параметры получает через поле `<text>`

```
<text>
цвет подсетки цикла (по умолчанию red)
удалять ли рёбра вне цикла? (по умолчанию false)
```

## Сборка  

```bash
pyinstaller make/make.spec
```