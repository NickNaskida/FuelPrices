from app.extensions import db


class BaseModel:
	"""
	SQLalchemy base model class

	attribs:
		- id: primary key

	methods:
		- Create
		- Read All
		- Update
		- Delete
		- Save
	"""

	id = db.Column(db.Integer, primary_key=True)

	def create(self, save=None, commit=None, **kwargs):
		for key, value in kwargs.items():
			setattr(self, key, value)

		if save is not None:
			self.save(commit=commit)

	@classmethod
	def read_all(cls):
		return cls.query.all()

	def update(self, save=None, commit=None, **kwargs):
		for key, value in kwargs.items():
			setattr(self, key, value)

		if save is not None:
			self.save(commit=commit)

	def delete(self):
		db.session.delete(self)
		db.session.commit()

	def save(self, commit=None):
		db.session.add(self)

		if commit is not None:
			db.session.commit()

	def __repr__(self):
		return f"< {self.__class__.__name__} model object >"

