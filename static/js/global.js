$(() => {
	pageTitleSorter();
	bsEvents();
})

function bsEvents() {
	$(window).resize(function () {
		var mql = window.matchMedia("(max-width: 600px)")
		if (mql.matches) {
			$('[data-toggle="tooltip"]').tooltip('show')
		}
	});
}
