---
aliases: [Dashboard, Home]
tags: []
---

# MathNotes Dashboard

## All Notes
```dataview
TABLE aliases AS "Title", tags, date
FROM "" AND -"_dashboard"
SORT date DESC
```

## By Tag
```dataview
TABLE length(rows) AS "Notes"
FROM "" AND -"_dashboard"
FLATTEN tags AS tag
GROUP BY tag
SORT length(rows) DESC
```

## Unresolved Links
```dataview
TABLE length(file.inlinks) AS "Referenced by", length(file.outlinks) AS "Links out"
FROM "" AND -"_dashboard"
SORT length(file.inlinks) DESC
```

## Recent Additions
```dataview
LIST
FROM "" AND -"_dashboard"
SORT file.ctime DESC
LIMIT 10
```
