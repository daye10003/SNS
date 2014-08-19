from application import app

app.config.update(dict(
    DEBUG=True,
    SECRET_KEY='development key',
    SQLALCHEMY_DATABASE_URI = 'mysql+gaerdbms:///sns?instance=daye100032:db',
    migration_directory = 'migrations'
))
