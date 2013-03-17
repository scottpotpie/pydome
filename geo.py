#! /usr/bin/env python
# -*- python -*-

#----------------------------------------------------------------
# References:
#   The calculations used in this program are all from the site
#   http://www.vb-helper.com/tutorial_platonic_solids.html
#   Many thanks for making this information available!
#
#----------------------------------------------------------------

import math
import Coordinates as C
import IcoFace as F
import GeoSphere as G
import config as CF

print "Coordinates"

#------------------------------------------------------------------
# Inputs

R_mm = 6000        # Radius of the circle in millimeters
frequency_n = 6     # Frequency of the geodesic

# Test case:
#       frequency_n = 1
#       
# Result:
#       Vertex count    = 18
#       Edge count      = 
#       Edge length     =

#------------------------------------------------------------------

#Centre angle of pentagon
t1_rad = 2 * math.pi / 5
t2_rad = math.pi / 10
t3_rad = -3 * math.pi / 10
t4_rad = math.pi / 5

S_mm = 2 * R_mm * math.sin(t4_rad)           # Side Length	
print "S = ", S_mm

H_mm= math.cos(t4_rad) * R_mm           # Height of triangle
print "Height of triangle: ", H_mm
Cx_mm = R_mm * math.cos(t2_rad)
Cy_mm = R_mm * math.sin(t2_rad)
	
H1_mm = math.sqrt( S_mm * S_mm - R_mm * R_mm )
print "H1: ", H1_mm
H2_mm = math.sqrt((H_mm+R_mm)*(H_mm+R_mm) - (H_mm*H_mm))
print "H2: ", H2_mm
	
Z2_mm = (H2_mm-H1_mm)/2          # Coordinate point (b-f)
print "Z2: ", Z2_mm
Z1_mm = Z2_mm + H1_mm          # Coordinate point (a)	
print "Z1: ", Z1_mm

#-------------------------------------------
# Icosahedron Coordinate Equations
#
# a = (   0,   0,  Z1)
# b = (   0,   R,  Z2)
# c = (  Cx,  Cy,  Z2)
# d = ( S/2,  -H,  Z2)
# e = (-S/2,  -H,  Z2)
# f = ( -Cx,  Cy,  Z2)
# g = (   0,  -R, -Z2)
# h = ( -Cx, -Cy, -Z2)
# i = (-S/2,   H, -Z2)
# j = ( S/2,   H, -Z2)
# k = (  Cx, -Cy, -Z2)
# l = (   0,   0, -Z1)

gs = G.GeoSphere("10m Dome", frequency_n, R_mm);

#VertexList = list()



# Test coordinates
#t1 = C.Coordinates("t1")
#t1.Set_Cartesian( -500, -500, 500 )
#t1.Set_Point_Number( CF.nPoint )
#CF.nPoint += 1
#gs.Add_Vertex(t1)

#t2 = C.Coordinates("t2")
#t2.Set_Cartesian( 500, -500, 500 )
#t2.Set_Point_Number( CF.nPoint )
#CF.nPoint += 1
#gs.Add_Vertex(t2)

#t3 = C.Coordinates("t3")
#t3.Set_Cartesian( 0, 500, 500 )
#t3.Set_Point_Number( CF.nPoint )
#CF.nPoint += 1
#gs.Add_Vertex(t3)



# Icosahedron vertice coordinates
a = C.Coordinates("a")
a.Set_Cartesian( 0, 0, Z1_mm )
a.Set_Point_Number( CF.nPoint )
CF.nPoint += 1
gs.Add_Vertex(a)

b = C.Coordinates("b")
b.Set_Cartesian( 0, R_mm, Z2_mm )
b.Set_Point_Number( CF.nPoint )
CF.nPoint += 1
gs.Add_Vertex(b)

c = C.Coordinates("c")
c.Set_Cartesian( Cx_mm, Cy_mm, Z2_mm)
c.Set_Point_Number( CF.nPoint )
CF.nPoint += 1
gs.Add_Vertex(c)

d = C.Coordinates("d")
d.Set_Cartesian( S_mm/2, -H_mm, Z2_mm)
d.Set_Point_Number( CF.nPoint )
CF.nPoint += 1
gs.Add_Vertex(d)

e = C.Coordinates("e")
e.Set_Cartesian(-S_mm/2, -H_mm, Z2_mm)
e.Set_Point_Number( CF.nPoint )
CF.nPoint += 1
gs.Add_Vertex(e)

f = C.Coordinates("f")
f.Set_Cartesian(-Cx_mm, Cy_mm, Z2_mm)
f.Set_Point_Number( CF.nPoint )
CF.nPoint += 1
gs.Add_Vertex(f)

g = C.Coordinates("g")
g.Set_Cartesian(0, -R_mm, -Z2_mm)
g.Set_Point_Number( CF.nPoint )
CF.nPoint += 1
gs.Add_Vertex(g)

h = C.Coordinates("h")
h.Set_Cartesian(-Cx_mm, -Cy_mm, -Z2_mm)
h.Set_Point_Number( CF.nPoint )
CF.nPoint += 1
gs.Add_Vertex(h)

i = C.Coordinates("i")
i.Set_Cartesian(-S_mm/2, H_mm, -Z2_mm)
i.Set_Point_Number( CF.nPoint )
CF.nPoint += 1
gs.Add_Vertex(i)

j = C.Coordinates("j")
j.Set_Cartesian(S_mm/2, H_mm, -Z2_mm)
j.Set_Point_Number( CF.nPoint )
CF.nPoint += 1
gs.Add_Vertex(j)

k = C.Coordinates("k")
k.Set_Cartesian(Cx_mm, -Cy_mm, -Z2_mm)
k.Set_Point_Number( CF.nPoint )
CF.nPoint += 1
gs.Add_Vertex(k)

l = C.Coordinates("l")
l.Set_Cartesian(0, 0, -Z1_mm)
l.Set_Point_Number( CF.nPoint )
CF.nPoint += 1
gs.Add_Vertex(l)


#------------------------------------------
# Add the 18 faces to the object
#
# Top 5 faces

# Test Face Only
#gs.Add_Face( t1, t2, t3 )


# Icosahedron faces

gs.Add_Face( a, b, c )


gs.Print_Vertices()
gs.Add_Face( a, c, d )
gs.Add_Face( a, d, e )
gs.Add_Face( a, e, f )
gs.Add_Face( a, f, b )

# Middle faces

gs.Add_Face( j, k, c )
gs.Add_Face( k, d, g )
gs.Add_Face( g, e, h )
gs.Add_Face( h, f, i )
gs.Add_Face( i, b, j )

gs.Add_Face( c, k, d )
gs.Add_Face( d, g, e )
gs.Add_Face( e, h, f )
gs.Add_Face( f, i, b )
gs.Add_Face( b, j, c )


# Bottom faces
gs.Add_Face( l, k, j )
gs.Add_Face( l, j, i )
gs.Add_Face( l, i, h )
gs.Add_Face( l, h, g )
gs.Add_Face( l, g, k )






# Set all the radius lenghts the same, ie project all points onto the sphere of radius Z1_mm
# If this is commented out then the points will be plotted on the original icosahedron




# Once all faces added, derive list of unique points
gs.Point_List_From_Edges()

# Create the list of edges with the new numbered and unique points
gs.Create_New_Edges()

# Remove duplicate edges as faces joining up will have the same edge
gs.Remove_Duplicate_Edges()

# DEBUG - print the raw hash of points
#print "Points Hash: " + str(gs.Point_Hash)

# Set all the points to have the same radius
gs.Set_Edges_Pt_Radius( R_mm )

#gs.Set_Edges_Pt_Radius( Z1_mm )


# For each point find the edges which meet there
gs.Hub_List_From_Edges()


# Print the CATIA details
# FIX: point this to use the points hash
gs.Print_Points()
gs.Print_Edges()
gs.Print_Vertices()


# Print the edges list??
#print "GS.POINT_LIST Printing\n"
#for a in gs.Point_List:
for a in gs.Point_Hash.keys():
    a.Print_Edges()

# Print the count of the hubs
gs.Count_Point_Intersections()

print "Hub count:", len(gs.Hub_Count)

print gs.Hub_Count


# Print the count of edge lengths
gs.Count_Edge_Lengths()

print "Length: ", len(gs.Edge_Count)

for b in gs.Edge_Count.keys():
    print "Length: " + str(b) + " - Count: " + str(gs.Edge_Count[b])
#print gs.Edge_Count


# Summary of data
print "Number of vertices: ", len(gs.Vertex_List)
print "Number of points: ", len(gs.Point_Hash.keys())
print "Number of edges: ", len(gs.Temp_Edge_List)
print "Final number of edges: ", len(gs.Edge_List)

#print sorted(gs.Edge_Count, key=lambda key: gs.Edge_Count[key])





