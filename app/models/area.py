from app import db

class Area(db.Model):
    __tablename__ = 'area'
    __table_args__ = {'sqlite_autoincrement': True}

    area_id = db.Column(db.Integer, unique=True, primary_key=True, nullable=False, autoincrement=True)
    ocd_id = db.Column(db.String, nullable=False)
    name = db.Column(db.String, nullable=False)
    country = db.Column(db.String, nullable=False)
    state = db.Column(db.String)
    city = db.Column(db.String)
    distric_type = db.Column(db.String, nullable=False)
    parent_area_id = db.Column(db.Integer, db.ForeignKey('area.area_id'), nullable=True)
    #area = relationship('Area', backref='area')

    def __init__(self, ocd_id, name, country, state, city, distric_type, parent_area_id):
        self.ocd_id = ocd_id
        self.name = name
        self.country = country
        self.state = state
        self.city = city
        self.distric_type = distric_type
        self.parent_area_id = parent_area_id

    def save(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def getAll():
        areas = Area.query.all()
        result = []
        for area in areas:
            obj = {
                'area_id': area.area_id,
                'ocd_id': area.ocd_id,
                'name': area.name,
                'country': area.country,
                'state': area.state,
                'city': area.city,
                'distric_type': area.distric_type,
                'parent_area_id': area.parent_area_id
            }
            result.append(obj)
        return result

    def delete(self):
        db.session.delete(self)
        db.session.commit()