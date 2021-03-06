# ##### BEGIN GPL LICENSE BLOCK #####
#
# (C) 2017 MKB
#
#  This program is free software; you can redistribute it and / or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110 - 1301, USA.
#
# ##### END GPL LICENSE BLOCK #####
#


# LOAD MODUL #    
import bpy
from bpy import *
from bpy.props import *


def draw_history_layout(context, layout):          
      
    layout.operator_context = 'INVOKE_REGION_WIN'

    box = layout.box().column(1)  

    row = box.row(1)        
    row.operator("ed.undo", text="Undo", icon="FRAME_PREV")  
    row.operator("ed.undo_history", text="History", icon="COLLAPSEMENU")
    row.operator("ed.redo", text="Redo", icon="FRAME_NEXT") 
   
    box.separator()                
    