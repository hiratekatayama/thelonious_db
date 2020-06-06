from collections import Counter

class Thelonious(object):
    # テーブル定義
    global tables
    tables = {}

    # リレーション
    class Relation(object):
        # 属性
        columns = []
        # データ
        taples = []

        def findColumn(self, name):
            global columns
            for i in range(len(columns)):
                if columns[i] == name:
                    return i
            return len(columns)

        def toString(self):
            global columns
            global taples
            pw = {}
            # フィールド名
            for c1 in columns:
                pw.add("|")
                if c1.parent != None and not c1.parent:
                    pw.add(c1.parent + ".")
                pw.add(c1.name)
            print("|")
            # データ
            for t in taples:
                for v in t.values:
                    pw.add("|")
                    pw.add(v)
                pw.add("|")
            return str(pw)

    class Table(Relation):
        __instance = None

        def __init__(cls, name, columns):
            cls.name = name
            cls.columns = columns
            taples = []

        @classmethod
        def __internal_new(cls):
            return super().__new__(cls)

        @classmethod
        def create(cls, name, columnsName):
            global t
            columns = []
            if not cls.__instance:
                cls.__instance = cls.__internal_new()
                for n in columnsName:
                    columns.append(Thelonious.Column(n))
                t = Thelonious.Table(name, columns)
                tables[name] = t
            return t

        def insert(self, *values):
            self.taples.append(Thelonious.Taple(values))

            return self

    # タプル
    class Taple(object):
        def __init__(self, *values):
            self.values = values

    # 属性
    class Column(object):
        def __init__(self, name, parent=""):
            self.name   = name
            self.parent = parent

