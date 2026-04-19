render-watchlist:
	python3 scripts/render_watchlist.py

render: render-watchlist
	quarto render docs

preview: render-watchlist
	quarto preview docs
