from asyncio import constants


glossary={
    "Tuple":"A fixed-value array",
    "List":"The most flexible collection data type",
    "Dictionary":"Associative array",
    "Append":"To add to the end of something",
    "Key:Value Pair":"Data structure organizing method",
    "Commit":"Confirm changes to",
    "Constant":"An unchanging variable, see variable",
    "Variable":"An adjustable constant, see constant",
    "Print":"Display value or text in terminal",
    ".lower":"Convert all latin characters to lowercase"
}
for g in glossary:
    print(g+":")
    print("\t",glossary[g])