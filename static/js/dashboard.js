$(function () {
	initCharts();
});

function bsEvents(){
	$('.onboarding-modal').modal('show');
}

function initCharts() {

	Chart.defaults.global.legend.labels.usePointStyle = true;

	var monthData = $('#id-month').data('month');
	var monthvalue = $('#id-value').data('value');

	monthData = monthData.substring(1, monthData.length - 1).split(', ')

	var regionData = $('#id-region').data('region');
	var regionCount = $('#id-count').data('count');

	regionData = regionData.substring(1, regionData.length - 1).split(', ')

	var specializations = $('#id-specializations').data('specializations');
	var app_count = $('#id-app_count').data('app_count');

	specializations = specializations.substring(1, specializations.length - 1).split(', ')

	var ctx = $('#bookings-chart');
	var ctx2 = $('#diseases-chart');
	var ctx3 = $('#recent-activity-chart');

	var recentActivitesChart = new Chart(ctx3, {
		type: 'line',
		data: {
			labels: monthData,
			datasets: [{
				label: '# of patients',
				data: monthvalue,
				backgroundColor: [
					'rgba(255, 99, 132, 0.7)',
					'rgba(54, 162, 235, 0.7)',
					'rgba(255, 206, 86, 0.7)',
					'rgba(75, 192, 192, 0.7)',
				],
			}],
		},
		options: {
			legend: {
				display: true,
				position: 'bottom',
			}
		},
	})
	var bookingsChart = new Chart(ctx, {
		type: 'doughnut',
		data: {
			labels: regionData,
			datasets: [{
				label: '# of Votes',
				data: regionCount,
				backgroundColor: [
					'rgba(255, 206, 86, 0.7)',
					'rgba(75, 192, 192, 0.7)',
					'rgba(54, 162, 235, 0.7)',
					'rgba(255, 99, 132, 0.7)',	
				],
			}],
		},
		options: {
			legend: {
				display: true,
				position: 'bottom',
			}
		},
	})
	var diseasesChart = new Chart(ctx2, {
		type: 'doughnut',
		data: {
			labels: specializations,
			datasets: [{
				label: '# of Votes',
				data: app_count,
				backgroundColor: [
					'rgba(255, 206, 86, 0.7)',
					'rgba(75, 192, 192, 0.7)',
					'rgba(54, 162, 235, 0.7)',
					'rgba(255, 99, 132, 0.7)',
				],
			}],
		},
		options: {
			legend: {
				display: true,
				position: 'bottom',
			}
		},
	})
}
