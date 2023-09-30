import sqlite3
#import basededatos
database = "basededatos.db"
class DB:
    def ejecutar_consulta(self,consulta,parametros=()):
        with sqlite3.connect(basededatos)as conn:
            self.cursor=conn.cursor()
            result = self.cursor.execute(consulta,parametros)
            conn.commit()
            return result
