from flask import Blueprint, render_template, request
from app.db import Session
from app.edit.forms import AccountDetail
from app.models import Account
from sqlalchemy import select, text
from app.user.models import User

edit = Blueprint("edit", __name__, template_folder="templates", static_folder="static")

@edit.route("/account", methods=["GET", "POST"])
def test():
    form = AccountDetail(request.form)
    if request.method == "POST" and form.validate():
        with Session() as session:
            add_account = Account(
              user_id = 1,
              name=form.account_name.data,
              currency=form.currency.data,
              symbol=form.symbol.data
              )
            session.add(add_account)
            session.commit()
    return render_template("edit/account.html", form=form)