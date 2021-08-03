import sqlite3

class CrawlPipeline(object):

    def __init__(self):
        self.create_conn()
        self.create_table()

    def create_conn(self):
        self.conn = sqlite3.connect("allmatch.db")
        self.curr = self.conn.cursor()

    def create_table(self):
        self.curr.execute("""create table if not exists app_allmatchs (
            team1 text,
            team2 text,
            data text
            )""")
    def process_item(self,item,spider):
       
        print("Pipelines = " + item['Team1'] + " "+item['Team2'] )

        self.curr.execute("""INSERT into app_allmatchs (team1, team2, data) values(?,?,?)""",(
            item['Team1'],
            item['Team2'],
            item['Data']
        ))
        self.conn.commit() 
        return item

        