# Copyright 2019 Kensho Technologies, LLC.
"""Mapping characters to ints to use as input to the character-level embedding layer."""

"""Ordering of characters in this dict follows that in https://github.com/zalandoresearch/flair
Any character not included will get mapped to <unk>, which in turn gets mapped to code 0."""
CHAR_TO_INT = {  # o
    "<unk>": 0,
    " ": 1,
    "e": 2,
    "n": 3,
    "i": 4,
    "t": 5,
    "a": 6,
    "r": 7,
    "s": 8,
    "o": 9,
    "h": 10,
    "d": 11,
    "l": 12,
    "u": 13,
    "c": 14,
    "m": 15,
    "g": 16,
    "\n": 17,
    ".": 18,
    "f": 19,
    "w": 20,
    "b": 21,
    "p": 22,
    ",": 23,
    "y": 24,
    "k": 25,
    "0": 26,
    "v": 27,
    "1": 28,
    "2": 29,
    "S": 30,
    "-": 31,
    "z": 32,
    ":": 33,
    "A": 34,
    "/": 35,
    "I": 36,
    "T": 37,
    "M": 38,
    "D": 39,
    "B": 40,
    "E": 41,
    "P": 42,
    "3": 43,
    "W": 44,
    "\u00fc": 45,
    "5": 46,
    "4": 47,
    "\u00e4": 48,
    "F": 49,
    ")": 50,
    "C": 51,
    "H": 52,
    "G": 53,
    "(": 54,
    "9": 55,
    "6": 56,
    "R": 57,
    "L": 58,
    "7": 59,
    "N": 60,
    "8": 61,
    "K": 62,
    "'": 63,
    "?": 64,
    '"': 65,
    "x": 66,
    "V": 67,
    "U": 68,
    "O": 69,
    "\u00f6": 70,
    "j": 71,
    "J": 72,
    "!": 73,
    "=": 74,
    "Z": 75,
    "\u00df": 76,
    "q": 77,
    "Y": 78,
    "*": 79,
    "_": 80,
    "+": 81,
    "\u20ac": 82,
    "%": 83,
    ";": 84,
    "]": 85,
    "&": 86,
    "[": 87,
    ">": 88,
    "#": 89,
    "\u2013": 90,
    "\u201c": 91,
    "\u00bb": 92,
    "\u2019": 93,
    "Q": 94,
    "X": 95,
    "\u201e": 96,
    "\u00ab": 97,
    "\u201d": 98,
    "\u00b0": 99,
    "\u00dc": 100,
    "\u00e9": 101,
    "\u00e1": 102,
    "<": 103,
    "\u00b2": 104,
    "\u00c3": 105,
    "\u00ff": 106,
    "$": 107,
    "\u00c7": 108,
    "\u00c4": 109,
    "\u2026": 110,
    "\u00d6": 111,
    "\\": 112,
    "\u2022": 113,
    "\u00ed": 114,
    "{": 115,
    "}": 116,
    "@": 117,
    "\u00a9": 118,
    "\u00e8": 119,
    "\u00bc": 120,
    "\u2018": 121,
    "\u00f3": 122,
    "\u2014": 123,
    "\u00c2": 124,
    "\u00c9": 125,
    "\u00ae": 126,
    "\u00b7": 127,
    "\u00e0": 128,
    "\u00f8": 129,
    "\u00d3": 130,
    "\u00b4": 131,
    "\u00da": 132,
    "\u00e2": 133,
    "~": 134,
    "\u00f1": 135,
    "\u00a4": 136,
    "\u00f0": 137,
    "\u00e5": 138,
    "\u00e7": 139,
    "\u266a": 140,
    "\u00e3": 141,
    "`": 142,
    "\u00b6": 143,
    "\u00a0": 144,
    "\u0161": 145,
    "\u00f4": 146,
    "\u00ee": 147,
    "\u0430": 148,
    "\u00f2": 149,
    "\u043e": 150,
    "\u0438": 151,
    "\u00a7": 152,
    "\u00eb": 153,
    "\u010d": 154,
    "\u00d7": 155,
    "\u2122": 156,
    "\u0101": 157,
    "\u00ec": 158,
    "\u00fa": 159,
    "\u0435": 160,
    "\u00b3": 161,
    "\u0440": 162,
    "\u00ea": 163,
    "\u043d": 164,
    "\u0442": 165,
    "\u203a": 166,
    "\u00ac": 167,
    "\u00e6": 168,
    "\u00fd": 169,
    "\u03bf": 170,
    "\u00a3": 171,
    "\u00d1": 172,
    "\u2020": 173,
    "\u0142": 174,
    "\u00c1": 175,
    "\u0131": 176,
    "\u00ef": 177,
    "\u00c8": 178,
    "\u0107": 179,
    "\u2192": 180,
    "\u017e": 181,
    "\u2032": 182,
    "\u0441": 183,
    "^": 184,
    "\u00c5": 185,
    "\u201a": 186,
    "\u00d8": 187,
    "\u00ce": 188,
    "\u0160": 189,
    "\u00cd": 190,
    "\u0159": 191,
    "\u043a": 192,
    "\u00cf": 193,
    "\u0432": 194,
    "\u043b": 195,
    "\u014d": 196,
    "\u011b": 197,
    "\u00ca": 198,
    "\u015f": 199,
    "\u00fb": 200,
    "\u00b1": 201,
    "\u0421": 202,
    "\u00a1": 203,
    "\u0434": 204,
    "\u00dd": 205,
    "\u043c": 206,
    "\u03b1": 207,
    "\u3002": 208,
    "\u0144": 209,
    "\u010c": 210,
    "\u00bd": 211,
    "\u00f5": 212,
    "\u00d5": 213,
    "\u00cc": 214,
    "\u012b": 215,
    "\u0443": 216,
    "\u0103": 217,
    "\u00c0": 218,
    "\u00ba": 219,
    "\u00d0": 220,
    "\u0431": 221,
    "\u00b5": 222,
    "\u25ba": 223,
    "\ufffd": 224,
    "\u00fe": 225,
    "\u0439": 226,
    "\u0627": 227,
    "\u011f": 228,
    "\u044c": 229,
    "\u016b": 230,
    "\u00f9": 231,
    "\u0437": 232,
    "\u00a8": 233,
    "\u03b2": 234,
    "\u017d": 235,
    "\u2212": 236,
    "\u0151": 237,
    "\u044f": 238,
    "\u0446": 239,
    "\u043f": 240,
    "\u0130": 241,
    "\u2011": 242,
    "\u03b9": 243,
    "\u03bd": 244,
    "\u00bf": 245,
    "\u0433": 246,
    "\u03c4": 247,
    "\u2039": 248,
    "\u03b5": 249,
    "\u00d4": 250,
    "\u00cb": 251,
    "\u0119": 252,
    "\u044b": 253,
    "\u00de": 254,
    "\u00d2": 255,
    "\u015b": 256,
    "\u00aa": 257,
    "\u0219": 258,
    "\u03c1": 259,
    "\u0105": 260,
    "\u0644": 261,
    "\u03bb": 262,
    "\u00b9": 263,
    "\u00f7": 264,
    "\u0449": 265,
    "\u0414": 266,
    "\u0447": 267,
    "\u03c2": 268,
    "\u7684": 269,
    "\u03bc": 270,
    "\u0445": 271,
    "\u016f": 272,
    "\u03c5": 273,
    "\u041f": 274,
}
