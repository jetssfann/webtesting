// //
// // FOR SOME REASON I CAN"T RUN THE TOASTER AND CHARTS AT THE SAME TIME
//
//
// // SELECT DOM ITEMS
//
// const menuBtn = document.querySelector('.menu-btn');
// const menu = document.querySelector('.menu');
// const menuNav = document.querySelector('.menu-nav');
// const menuBranding = document.querySelector('.menu-branding');
//
// const navItems = document.querySelectorAll ('.nav-item');
//
// //Set Initial state of menuBtn
//
// let showMenu = false;
//
// menuBtn.addEventListener('click', toggleMenu);
//
// function toggleMenu () {
//   if(!showMenu) {
//     menuBtn.classList.add('close');
//     menu.classList.add('show');
//     menuNav.classList.add('show');
//     menuBranding.classList.add('show');
//
//     navItems.forEach(item => item.classList.add ('show'));
//
//     //Set Menu state
//     showMenu = true;
//   } else {
//     menuBtn.classList.remove('close');
//     menu.classList.remove('show');
//     menuNav.classList.remove('show');
//     menuBranding.classList.remove('show');
//
//     navItems.forEach(item => item.classList.add ('close'));
//
//     //Set Menu state
//     showMenu = false;
//
//   }
// };
//
// Chart.defaults.global.plugins.datalabels.display = function(ctx) {
//   return ctx.value !== 0;
// };

let myretentionChart = document.getElementById('myretentionChart').getContext('2d');

let retentionChart = new Chart(myretentionChart, {
  type:'doughnut',
  data:{
    labels:['New', 'Returning'],
    datasets:[{
      label:'Teams',
      data:[302,191],
      backgroundColor:['yellow','purple'],
      borderWidth:1,
      borderColor:'black'
    }]
  },
  options:{
    legend: {
      labels:{
        fontColor: '#fff',
      }
    }
  }
})

let mykpiChart = document.getElementById('mykpiChart').getContext('2d');

let kpiChart = new Chart(mykpiChart, {
  type:'doughnut',
  data:{
    labels:[ 'Wait Listed', 'Registered', 'Remaining'],
    datasets:[{
      label:'Teams',
      data:[555-550,550,550-550],
      backgroundColor:['blue','green','red'],
      borderWidth:1,
      borderColor:'black'
    }]
  },
  options:{
    legend: {
      labels:{
        fontColor: '#fff',
      }
    },
    plugins: {
      datalabels: {
        display: function(context) {
        var index = context.dataIndex;
        var value = context.dataset.data[0];
        return value <= 0 ? 'true' :  // draw negative values in red
            index % 2 ? 'blue' :    // else, alternate values in blue and green
            'green';
    },
     },
    },
  }
});


let mystateChart = document.getElementById('mystateChart').getContext('2d');

let stateChart = new Chart(mystateChart, {
  type:'bar',
  data:{
    labels:['NJ','PAE','NYE','MD','VA'],
    datasets:[{
      label:'Teams',
      data:[225,58,114,48,5],
      backgroundColor:['green','red','yellow','blue','orange'],
      borderWidth:0,
      borderColor:'black'
    }]
  },
  options:{
    legend: {
      display: false,
    }
  }
});


// let mylineChart = document.getElementById('mylineChart').getContext('2d');
//
// let retentionlineChart = new Chart(mylineChart, {
//   type:'line',
//   data:{
//     labels:['2016','2017','2018','2019','2020'],
//     datasets:[{
//       data:[40,60,80,75,69],
//       backgroundColor:['blue'],
//       borderWidth:3,
//       borderColor:'white'
//     }]
//   },
//   options:{
//     legend:{
//       display: false
//       },
//     scales:{
//       xAxes:[{
//         gridLines:{
//           display: false
//           }
//         }],
//         yAxes:[{
//           // angleLines:{
//           //   display:false
//           // },
//           gridLines:{
//             display: false
//             }
//           }]
//       },
//     }
//   });

// Chart Setup
