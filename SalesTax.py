print('The Python United States Sales Tax Calculator.')

print('Enter Price Without Dollar Sign and State Below')

Colorado = 0.029

Alabama = 0.04

Georgia = 0.04

Guam = 0.04

New_York = 0.04

South_Dakota = 0.04

Wyoming = 0.04

Hawaii = 0.04

Missouri = 0.04225

Louisiana = 0.045

Oklahoma = 0.045

North_Carolina = 0.0475

North_Dakota = .05

Wisconsin = .05

New_Mexico = 0.05125					

Virginia = 0.053				

Maine =	0.055	

Nebraska = 0.055			

Arizona = 0.056						

District_Of_Columbia = 0.0575				

Ohio = 0.0575			

Utah = 0.0595					

Florida = 0.06				

Idaho = 0.06			

Iowa = 0.06					

Kentucky = 0.06						

Maryland = 0.06						

Michigan = 0.06							

Pennsylvania = 0.06							

South_Carolina = 0.06					

Vermont =  0.06							

West_Virginia = 0.06							

Illinois =  0.0625			

Massachusetts = 0.0625	

Texas =	0.0625						

Connecticut = 0.0635						

Arkansas = 0.065					

Kansas = 0.065						

Washington = 0.065				

New_Jersey = 0.06625					

Nevada = 0.0685						

Minnesota = 0.06875					

Indiana = 0.07				

Mississippi = 0.07					

Rhode_Island = 0.07

Tennessee = 0.07				

California = 0.0725					

Puerto_Rico = 0.105


Price = input('Enter Price:')

State = input('Enter State: ')

# enter this at end: if State == "Alaska" or "Delaware" or "Montana" or "New Hampshire" or "Oregon": print('This State Does Not Have State Mandated Sales Tax') else: pass

if State == "Colorado":

    print('Sales Tax Rate For Colorado: 2.9%')

    print("Subtotal: $" + Price)

    Colorado_Tax = int(Price) * Colorado

    print(f"Sales Tax: ${Colorado_Tax:.2f}")

    Colorado_Total = int(Price) + Colorado_Tax

    print(f"Total: ${Colorado_Total:.2f}")



if State == "Alabama":

    print('Sales Tax Rate For Alabama: 4%')

    print("Subtotal: $" + Price)

    Alabama_Tax = int(Price) * Alabama

    print(f"Sales Tax: ${Alabama_Tax:.2f}")

    Alabama_Total = int(Price) + Alabama_Tax

    print(f"Total: ${Alabama_Total:.2f}")



if State == "Georgia":

    print('Sales Tax Rate For Georgia: 4%')

    print("Subtotal: $" + Price)

    Georgia_Tax = int(Price) * Georgia

    print(f"Sales Tax: ${Georgia_Tax:.2f}")

    Georgia_Total = int(Price) + Georgia_Tax

    print(f"Total: ${Georgia_Total:.2f}")



if State == "New York":

    print('Sales Tax Rate For New York: 4%')

    print("Subtotal: $" + Price)

    New_York_Tax = int(Price) * New_York

    print(f"Sales Tax: ${New_York_Tax:.2f}")

    New_York_Total = int(Price) + New_York_Tax

    print(f"Total: ${New_York_Total:.2f}")



if State == "South Dakota":

    print('Sales Tax Rate For South Dakota: 4%')

    print("Subtotal: $" + Price)

    South_Dakota_Tax = int(Price) * South_Dakota

    print(f"Sales Tax: ${South_Dakota_Tax:.2f}")

    South_Dakota_Total = int(Price) + South_Dakota_Tax

    print(f"Total: ${South_Dakota_Total:.2f}")



if State == "Wyoming":

    print('Sales Tax Rate For Wyoming: 4%')

    print("Subtotal: $" + Price)

    Wyoming_Tax = int(Price) * Wyoming

    print(f"Sales Tax: ${Wyoming_Tax:.2f}")

    Wyoming_Total = int(Price) + Wyoming_Tax

    print(f"Total: ${Wyoming_Total:.2f}")



if State == "Hawaii":

    print('Sales Tax Rate For Hawaii: 4%')

    print("Subtotal: $" + Price)

    Hawaii_Tax = int(Price) * Hawaii

    print(f"Sales Tax: ${Hawaii_Tax:.2f}")

    Hawaii_Total = int(Price) + Hawaii_Tax

    print(f"Total: ${Hawaii_Total:.2f}")



if State == "Missouri":

    print('Sales Tax Rate For Missouri: 4.225%')

    print("Subtotal: $" + Price)

    Missouri_Tax = int(Price) * Missouri

    print(f"Sales Tax: ${Missouri_Tax:.2f}")

    Missouri_Total = int(Price) + Missouri_Tax

    print(f"Total: ${Missouri_Total:.2f}")



if State == "Louisiana":

    print('Sales Tax Rate For Louisiana: 4.45%')

    print("Subtotal: $" + Price)

    Louisiana_Tax = int(Price) * Louisiana

    print(f"Sales Tax: ${Louisiana_Tax:.2f}")

    Louisiana_Total = int(Price) + Louisiana_Tax

    print(f"Total: ${Louisiana_Total:.2f}")



if State == "Oklahoma":

    print('Sales Tax Rate For Oklahoma: 4.5%')

    print("Subtotal: $" + Price)

    Oklahoma_Tax = int(Price) * Oklahoma

    print(f"Sales Tax: ${Oklahoma_Tax:.2f}")

    Oklahoma_Total = int(Price) + Oklahoma_Tax

    print(f"Total: ${Oklahoma_Total:.2f}")



if State == "North Carolina":

    print('Sales Tax Rate For North Carolina: 4.75%')

    print("Subtotal: $" + Price)

    North_Carolina_Tax = int(Price) * North_Carolina

    print(f"Sales Tax: ${North_Carolina_Tax:.2f}")

    North_Carolina_Total = int(Price) + North_Carolina_Tax

    print(f"Total: ${North_Carolina_Total:.2f}")



if State == "North Dakota":

    print('Sales Tax Rate For North Dakota: 5%')

    print("Subtotal: $" + Price)

    North_Dakota_Tax = int(Price) * North_Dakota

    print(f"Sales Tax: ${North_Dakota_Tax:.2f}")

    North_Dakota_Total = int(Price) + North_Dakota_Tax

    print(f"Total: ${North_Dakota_Total:.2f}")



if State == "Wisconsin":

    print('Sales Tax Rate For Wisconsin: 5%')

    print("Subtotal: $" + Price)

    Wisconsin_Tax = int(Price) * Wisconsin

    print(f"Sales Tax: ${Wisconsin_Tax:.2f}")

    Wisconsin_Total = int(Price) + Wisconsin_Tax

    print(f"Total: ${Wisconsin_Total:.2f}")



if State == "New Mexico":

    print('Sales Tax Rate For New Mexico: 5.125%')

    print("Subtotal: $" + Price)

    New_Mexico_Tax = int(Price) * New_Mexico

    print(f"Sales Tax: ${New_Mexico_Tax:.2f}")

    New_Mexico_Total = int(Price) + New_Mexico_Tax

    print(f"Total: ${New_Mexico_Total:.2f}")



if State == "Virginia":

    print('Sales Tax Rate For Virginia: 5.3%')

    print("Subtotal: $" + Price)

    Virginia_Tax = int(Price) * Virginia

    print(f"Sales Tax: ${Virginia_Tax:.2f}")

    Virginia_Total = int(Price) + Virginia_Tax

    print(f"Total: ${Virginia_Total:.2f}")



if State == "Maine":

    print('Sales Tax Rate For Maine: 5.5%')

    print("Subtotal: $" + Price)

    Maine_Tax = int(Price) * Maine

    print(f"Sales Tax: ${Maine_Tax:.2f}")

    Maine_Total = int(Price) + Maine_Tax

    print(f"Total: ${Maine_Total:.2f}")


    
if State == "Nebraska":

    print('Sales Tax Rate For Nebraska: 5.5%')

    print("Subtotal: $" + Price)

    Nebraska_Tax = int(Price) * Nebraska

    print(f"Sales Tax: ${Nebraska_Tax:.2f}")

    Nebraska_Total = int(Price) + Nebraska_Tax

    print(f"Total: ${Nebraska_Total:.2f}")



if State == "Arizona":

    print('Sales Tax Rate For Arizona: 5.6%')

    print("Subtotal: $" + Price)

    Arizona_Tax = int(Price) * Arizona

    print(f"Sales Tax: ${Arizona_Tax:.2f}")

    Arizona_Total = int(Price) + Arizona_Tax

    print(f"Total: ${Arizona_Total:.2f}") 

    

if State == "Ohio":

    print('Sales Tax Rate For Ohio: 5.75%')

    print("Subtotal: $" + Price)

    Ohio_Tax = int(Price) * Ohio

    print(f"Sales Tax: ${Ohio_Tax:.2f}")

    Ohio_Total = int(Price) + Ohio_Tax

    print(f"Total: ${Ohio_Total:.2f}")



if State == "Utah":

    print('Sales Tax Rate For Utah: 5.95%')

    print("Subtotal: $" + Price)

    Utah_Tax = int(Price) * Utah

    print(f"Sales Tax: ${Utah_Tax:.2f}")

    Utah_Total = int(Price) + Utah_Tax

    print(f"Total: ${Utah_Total:.2f}")



if State == "Florida":

    print('Sales Tax Rate For Florida: 6%')

    print("Subtotal: $" + Price)

    Florida_Tax = int(Price) * Florida

    print(f"Sales Tax: ${Florida_Tax:.2f}")

    Florida_Total = int(Price) + Florida_Tax

    print(f"Total: ${Florida_Total:.2f}")



if State == "Idaho":

    print('Sales Tax Rate For Idaho: 6%')

    print("Subtotal: $" + Price)

    Idaho_Tax = int(Price) * Idaho

    print(f"Sales Tax: ${Idaho_Tax:.2f}")

    Idaho_Total = int(Price) + Idaho_Tax

    print(f"Total: ${Idaho_Total:.2f}")



if State == "Iowa":

    print('Sales Tax Rate For Iowa: 6%')

    print("Subtotal: $" + Price)

    Iowa_Tax = int(Price) * Iowa

    print(f"Sales Tax: ${Iowa_Tax:.2f}")

    Iowa_Total = int(Price) + Iowa_Tax

    print(f"Total: ${Iowa_Total:.2f}")



if State == "Kentucky":

    print('Sales Tax Rate For Kentucky: 6%')

    print("Subtotal: $" + Price)

    Kentucky_Tax = int(Price) * Kentucky

    print(f"Sales Tax: ${Kentucky_Tax:.2f}")

    Kentucky_Total = int(Price) + Kentucky_Tax

    print(f"Total: ${Kentucky_Total:.2f}")


if State == "Maryland":

    print('Sales Tax Rate For Maryland: 6%')

    print("Subtotal: $" + Price)

    Maryland_Tax = int(Price) * Maryland

    print(f"Sales Tax: ${Maryland_Tax:.2f}")

    Maryland_Total = int(Price) + Maryland_Tax

    print(f"Total: ${Maryland_Total:.2f}")


if State == "Michigan":

    print('Sales Tax Rate For Michigan: 6%')

    print("Subtotal: $" + Price)

    Michigan_Tax = int(Price) * Michigan

    print(f"Sales Tax: ${Michigan_Tax:.2f}")

    Michigan_Total = int(Price) + Michigan_Tax

    print(f"Total: ${Michigan_Total:.2f}")


if State == "Pennsylvania":

    print('Sales Tax Rate For Pennsylvania: 6%')

    print("Subtotal: $" + Price)

    Pennsylvania_Tax = int(Price) * Pennsylvania

    print(f"Sales Tax: ${Pennsylvania_Tax:.2f}")

    Pennsylvania_Total = int(Price) + Pennsylvania_Tax

    print(f"Total: ${Pennsylvania_Total:.2f}")


if State == "South Carolina":

    print('Sales Tax Rate For South Carolina: 6%')

    print("Subtotal: $" + Price)

    South_Carolina_Tax = int(Price) * South_Carolina

    print(f"Sales Tax: ${South_Carolina_Tax:.2f}")

    South_Carolina_Total = int(Price) + South_Carolina_Tax

    print(f"Total: ${South_Carolina_Total:.2f}")


if State == "Vermont":

    print('Sales Tax Rate For Vermont: 6%')

    print("Subtotal: $" + Price)

    Vermont_Tax = int(Price) * Vermont

    print(f"Sales Tax: ${Vermont_Tax:.2f}")

    Vermont_Total = int(Price) + Vermont_Tax

    print(f"Total: ${Vermont_Total:.2f}")


if State == "West Virginia":

    print('Sales Tax Rate For West Virginia: 6%')

    print("Subtotal: $" + Price)

    West_Virginia_Tax = int(Price) * West_Virginia

    print(f"Sales Tax: ${West_Virginia_Tax:.2f}")

    West_Virginia_Total = int(Price) + West_Virginia_Tax

    print(f"Total: ${West_Virginia_Total:.2f}")



if State == "Illinois":

    print('Sales Tax Rate For Illinois: 6.25%')

    print("Subtotal: $" + Price)

    Illinois_Tax = int(Price) * Illinois

    print(f"Sales Tax: ${Illinois_Tax:.2f}")

    Illinois_Total = int(Price) + Illinois_Tax

    print(f"Total: ${Illinois_Total:.2f}")


if State == "Massachusetts":

    print('Sales Tax Rate For Massachusetts: 6.25%')

    print("Subtotal: $" + Price)

    Massachusetts_Tax = int(Price) * Massachusetts

    print(f"Sales Tax: ${Massachusetts_Tax:.2f}")

    Massachusetts_Total = int(Price) + Massachusetts_Tax

    print(f"Total: ${Massachusetts_Total:.2f}")


if State == "Texas":

    print('Sales Tax Rate For Texas: 6.25%')

    print("Subtotal: $" + Price)

    Texas_Tax = int(Price) * Texas

    print(f"Sales Tax: ${Texas_Tax:.2f}")

    Texas_Total = int(Price) + Texas_Tax

    print(f"Total: ${Texas_Total:.2f}")


if State == "Connecticut":

    print('Sales Tax Rate For Connecticut: 6.35%')

    print("Subtotal: $" + Price)

    Connecticut_Tax = int(Price) * Connecticut

    print(f"Sales Tax: ${Connecticut_Tax:.2f}")

    Connecticut_Total = int(Price) + Connecticut_Tax

    print(f"Total: ${Connecticut_Total:.2f}")


if State == "Arkansas":

    print('Sales Tax Rate For Arkansas: 6.5%')

    print("Subtotal: $" + Price)

    Arkansas_Tax = int(Price) * Arkansas

    print(f"Sales Tax: ${Arkansas_Tax:.2f}")

    Arkansas_Total = int(Price) + Arkansas_Tax

    print(f"Total: ${Arkansas_Total:.2f}")


if State == "Kansas":

    print('Sales Tax Rate For Kansas: 6.5%')

    print("Subtotal: $" + Price)

    Kansas_Tax = int(Price) * Kansas

    print(f"Sales Tax: ${Kansas_Tax:.2f}")

    Kansas_Total = int(Price) + Kansas_Tax

    print(f"Total: ${Kansas_Total:.2f}")


if State == "Washington":

    print('Sales Tax Rate For Washington: 6.5%')

    print("Subtotal: $" + Price)

    Washington_Tax = int(Price) * Washington

    print(f"Sales Tax: ${Washington_Tax:.2f}")

    Washington_Total = int(Price) + Washington_Tax

    print(f"Total: ${Washington_Total:.2f}")


if State == "New Jersey":

    print('Sales Tax Rate For New Jersey: 6.625%')

    print("Subtotal: $" + Price)

    New_Jersey_Tax = int(Price) * New_Jersey

    print(f"Sales Tax: ${New_Jersey_Tax:.2f}")

    New_Jersey_Total = int(Price) + New_Jersey_Tax

    print(f"Total: ${New_Jersey_Total:.2f}")


if State == "Nevada":

    print('Sales Tax Rate For Nevada: 6.85%')

    print("Subtotal: $" + Price)

    Nevada_Tax = int(Price) * Nevada

    print(f"Sales Tax: ${Nevada_Tax:.2f}")

    Nevada_Total = int(Price) + Nevada_Tax

    print(f"Total: ${Nevada_Total:.2f}")

if State == "Minnesota":

    print('Sales Tax Rate For Minnesota: 6.875%')

    print("Subtotal: $" + Price)

    Minnesota_Tax = int(Price) * Minnesota

    print(f"Sales Tax: ${Minnesota_Tax:.2f}")

    Minnesota_Total = int(Price) + Minnesota_Tax

    print(f"Total: ${Minnesota_Total:.2f}")


if State == "Indiana":

    print('Sales Tax Rate For Indiana: 7%')

    print("Subtotal: $" + Price)

    Indiana_Tax = int(Price) * Indiana

    print(f"Sales Tax: ${Indiana_Tax:.2f}")

    Indiana_Total = int(Price) + Indiana_Tax

    print(f"Total: ${Indiana_Total:.2f}")


if State == "Mississippi":

    print('Sales Tax Rate For Mississippi: 7%')

    print("Subtotal: $" + Price)

    Mississippi_Tax = int(Price) * Mississippi

    print(f"Sales Tax: ${Mississippi_Tax:.2f}")

    Mississippi_Total = int(Price) + Mississippi_Tax

    print(f"Total: ${Mississippi_Total:.2f}")


if State == "Rhode Island":

    print('Sales Tax Rate For Rhode Island: 7%')

    print("Subtotal: $" + Price)

    Rhode_Island_Tax = int(Price) * Rhode_Island

    print(f"Sales Tax: ${Rhode_Island_Tax:.2f}")

    Rhode_Island_Total = int(Price) + Rhode_Island_Tax

    print(f"Total: ${Rhode_Island_Total:.2f}")


if State == "Tennessee":

    print('Sales Tax Rate For Tennessee: 7%')

    print("Subtotal: $" + Price)

    Tennessee_Tax = int(Price) * Tennessee

    print(f"Sales Tax: ${Tennessee_Tax:.2f}")

    Tennessee_Total = int(Price) + Tennessee_Tax

    print(f"Total: ${Tennessee_Total:.2f}")


if State == "California":

    print('Sales Tax Rate For California: 7.25%')

    print("Subtotal: $" + Price)

    California_Tax = int(Price) * California

    print(f"Sales Tax: ${California_Tax:.2f}")

    California_Total = int(Price) + California_Tax

    print(f"Total: ${California_Total:.2f}")

#nixKodes num.003