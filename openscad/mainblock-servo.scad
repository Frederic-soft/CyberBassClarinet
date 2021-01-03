difference () {
  cube(size=[30, 25, 50]);
  translate([2,-1,5]) cube(size=[26, 18, 40]);  // hollow cube
  translate([15, 38, -1]) cylinder(h=93, r=20, $fn=200);  // clarinet body
  translate([-7, 4, 10]) cube(size=[22, 12.5, 25]);  // servo
  translate([2.5, 4.9, 2.5]) rotate([90,0,0]) cylinder(h=5, r=0.5, $fn=100);
  translate([27.5, 4.9, 2.5]) rotate([90,0,0]) cylinder(h=5, r=0.5, $fn=100);
  translate([27.5, 4.9, 47.5]) rotate([90,0,0]) cylinder(h=5, r=0.5, $fn=100);
  translate([2.5, 4.9, 47.5]) rotate([90,0,0]) cylinder(h=5, r=0.5, $fn=100);
};
