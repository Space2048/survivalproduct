from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
# from werkzeug.exceptions import abort

# from flaskr.auth import login_required
# from flaskr.db import get_db
from service import pigstyService



pigstyBp = Blueprint('pigsty', __name__)


@pigstyBp.router("/")
def test():
    return "test"