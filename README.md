# "entascope" - A Scope for Named Entities

Use the entascope to identify and extract named entities from news outlets' websites. 

This is a work in progress. 

Right now you can extract entities from NPR, FOX, and MSNBC. Documentation will be added later.

## Description of Named spaCy's Named Entity Labels

| Label  | Description |
| ------------- | ------------- |
| `PERSON`  | People, including fictional.  |
| `NORP`  | Nationalities or religious or political groups.  |
| `FAC` | Buildings, airports, highways, bridges, etc. |
| `ORG` | Companies, agencies, institutions, etc. |
| `GPE` | Countries, cities, states. |
| `LOC` | Non-GPE locations, mountain ranges, bodies of water. |
| `PRODUCT` | Objects, vehicles, foods, etc. (Not services.) |
| `EVENT` | Wars, sports events, etc. |
| `WORK_OF_ART` | Titles of books, songs, etc. |
| `LAW` | Named documents made into laws. |
| `LANGUAGE` | Any named language. |
| `DATE` | Absolute or relative dates or periods. |
| `TIME` | Times smaller than a day. |
| `PERCENT` | Percentage, including "%". |
| `MONEY` | Monetary values, including unit. |
| `QUANTITY` | Measurements such as weight or distance. |
| `ORDINAL` | Ordered data such as "first," "second," etc. |
| `CARDINAL` | Numerals that do not fall under another type. |
