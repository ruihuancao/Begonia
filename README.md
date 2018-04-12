# Begonia 

---

### 使用库

- pipenv
- Flask
- falsk-restful

#### flask-sqlalchemy 数据库ORM
http://www.pythondoc.com/flask-sqlalchemy/quickstart.html

创建表
```
from app import db
db.create_all()
```

#### flask-migrate   数据库升级
https://flask-migrate.readthedocs.io/en/latest/

```
python manager.py db init # 初始化
python manager.py db migrate # 创建迁移脚本
python manager.py db upgrade # 更新到数据库中

```


