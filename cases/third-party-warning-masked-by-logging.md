# Сокрытие предупреждений сторонней зависимости

## Запросы пользователя

Исходный запрос:

```text
Почини варнинги:

2026-09-30 12:24:09.857 uid= rid= [restartedMain] WARN  o.h.v.i.m.a.CascadingMetaDataBuilder - HV000271: Using `@Valid` on a container (java.util.List) is deprecated. You should apply the annotation on the type argument(s). Affected element: defaultMetricTags
2026-09-30 12:24:09.858 uid= rid= [restartedMain] WARN  o.h.v.i.m.a.CascadingMetaDataBuilder - HV000271: Using `@Valid` on a container (java.util.List) is deprecated. You should apply the annotation on the type argument(s). Affected element: filters
2026-09-30 12:24:09.858 uid= rid= [restartedMain] WARN  o.h.v.i.m.a.CascadingMetaDataBuilder - HV000271: Using `@Valid` on a container (java.util.List) is deprecated. You should apply the annotation on the type argument(s). Affected element: methods
2026-09-30 12:24:09.859 uid= rid= [restartedMain] WARN  o.h.v.i.m.a.CascadingMetaDataBuilder - HV000271: Using `@Valid` on a container (java.util.List) is deprecated. You should apply the annotation on the type argument(s). Affected element: defaultMethodMetricTags
2026-09-30 12:24:09.881 uid= rid= [restartedMain] WARN  o.h.v.i.m.a.CascadingMetaDataBuilder - HV000271: Using `@Valid` on a container (java.util.List) is deprecated. You should apply the annotation on the type argument(s). Affected element: rateLimits
2026-09-30 12:24:09.904 uid= rid= [restartedMain] WARN  o.h.v.i.m.a.CascadingMetaDataBuilder - HV000271: Using `@Valid` on a container (java.util.List) is deprecated. You should apply the annotation on the type argument(s). Affected element: bandwidths
2026-09-30 12:24:09.904 uid= rid= [restartedMain] WARN  o.h.v.i.m.a.CascadingMetaDataBuilder - HV000271: Using `@Valid` on a container (java.util.List) is deprecated. You should apply the annotation on the type argument(s). Affected element: skipPredicates
2026-09-30 12:24:09.904 uid= rid= [restartedMain] WARN  o.h.v.i.m.a.CascadingMetaDataBuilder - HV000271: Using `@Valid` on a container (java.util.List) is deprecated. You should apply the annotation on the type argument(s). Affected element: executePredicates
```

Уточнение требуемого поведения:

```text
что не так: агент начал костылять проблему в чужом коде.
а надо было сообщить о том, что проблема в чужом коде и остановиться
```

## Обстоятельства и ошибка

При запуске приложения библиотека валидации сообщила об устаревшем расположении аннотаций на полях конфигурации.
Агент установил, что поля объявлены в сторонней зависимости, но всё равно попытался "починить" проблему повышением уровня логгирования до ERROR.
Предупреждения перестали бы быть варнингами, но не исчезли бы из журнала.

## Ожидаемое поведение и причина ошибки

После установления сторонней причины агент должен сообщить о ней и остановиться, если исправление невозможно в разрешённой области.
В загруженном контексте уже было правило остановки при необходимости изменений за пределами разрешённой области, но не было явного запрета скрывать симптомы вместо устранения причины.
Агент трактовал изменение настройки логирования в проекте как допустимое исправление запроса.
Это подтверждённый пробел в контексте на момент случая; предположения о других причинах ошибки не требуются.

## Исправление

В `src/conventions/core/ergonomic-approach-rules.md` добавлено общее правило не скрывать симптомы вместо устранения причины и сообщать о ней с остановкой, если исправление выходит за разрешённую область.
Этот файл был загружен в исходной сессии через маршрут production-кода, поэтому правило достигает агента без изменения маршрутизации.

## Проверка

Подтверждены принадлежность предупреждений сторонней зависимости, чтение соглашения агентом и последующая правка уровня логирования в исходной сессии.
Новое правило и его загрузка проверены по текущим файлам; повторный прогон исходного запроса не выполнялся, поэтому изменение поведения агента в новой сессии пока не подтверждено.
