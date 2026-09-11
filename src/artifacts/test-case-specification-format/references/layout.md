# Разметка

Используйте эту разметку для каждого вывода `test-case-specification-format`.

- `Feature` начинается в столбце `0`.
- Добавляйте к `Feature` показанную ниже SUT-ссылку в скобках.
- Ставьте одну пустую строку после `Feature` перед его первым `Rule`.
- Делайте отступ `Rule` на `2` пробела под его `Feature`.
- Делайте отступ `Example` и ссылок на источник, принадлежащих `Rule`, на `4` пробела под их `Rule`.
- Делайте отступ ссылок на источник, принадлежащих `Example`, и шагов полного режима на `6` пробелов под их `Example`.
- Используйте ссылки на источник, принадлежащие `Rule`, только когда `Example` не выводится.
- Выводите безымянные примеры полного режима как `Example`.
- Если у `Rule` есть безымянный `Example`, этот безымянный пример должен быть единственным `Example` в этом `Rule`.
- Размещайте `Example` сразу под `Rule`.
- Размещайте ссылки на источник и шаги полного режима сразу под их владельцем, без пустой строки.
- Разделяйте соседние блоки `Rule` и `Feature` одной пустой строкой.
- Если формат чата требует префикс роли, размещайте артефакт со следующей строки и сохраняйте `Feature` в столбце `0`.

```text
Feature: <human-readable verified object> (<SUT reference>)

  Rule: <required property>
    Example: <optional semantic input or context class, or empty>
      # <commit>:<relative-file-path>:<line-number>
      Given <relevant condition>
      When <action on the Feature>
      Then <observable result>
```
