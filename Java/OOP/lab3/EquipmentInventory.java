package OOP.lab3;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.Map;
import OOP.lab3.Equipment;
/** 
 * Finish this class.
 */
public class EquipmentInventory {

	/** The list of all your equipment objects */
	ArrayList<Equipment> inventory;
	/** The number of objects per type of equipment, grouped by the String description of a type */
	HashMap<String, Integer> inventoryCount;

	/** 
	 * Create an EquipmentInventory object by initializing the inventory and inventoryCount objects.
	 */
	public EquipmentInventory() {
		inventory = new ArrayList<Equipment>();
		inventoryCount = new HashMap<String, Integer>();
	}

	/**
	 * Add e to the inventory, and if the add is successful, increase the number of that equipment type in your inventoryCount.
	 * Make sure that you cannot accidentally add the same object twice.
	 * @param e The equipment object to add
	 */
	public void add(Equipment e) {
		if (inventory.contains(e)){
            increaseInventoryCount(e);
        }else{
            inventory.add(e);
            increaseInventoryCount(e);
        }
	}

	/**
	 * Remove e from the inventory and if successful, decrease the number of that equipment type in your inventoryCount.
	 * @param e The equipment object to remove
	 */
	public void remove(Equipment e) {
		inventory.remove(e);
        decreaseInventoryCount(e);
	}

	/**
	 * Increase the inventoryCount for the type of equipment of e by 1.
	 * If it does not exist in the inventoryCount yet, add the type to the inventoryCount.
	 * Note: this method should be private, but to allow running unit tests on it (and make our lives easier when marking),
	 * we made this method protected. The method should never be called outside of the class. 	 
	 * @param e The type of equipment for which we want to increase the inventoryCount
	 */
	protected void increaseInventoryCount(Equipment e) {
		if (inventoryCount.containsKey(e.toString())){
            inventoryCount.put(e.toString(),getInventoryCount(e)+1);
        }else{
            inventoryCount.put(e.toString(),1);
        }
	}

	/**
	 * Decrease the inventoryCount for the type of equipment of e by 1.
	 * If the inventoryCount for this type is now 0, remove the type from the inventoryCount.
	 * If the inventoryCount does not contain this type of equipment, do nothing.
	 * Note: this method should be private, but to allow running unit tests on it (and make our lives easier when marking),
	 * we made this method protected. The method should never be called outside of the class. 	 
	 * @param e The type of equipment for which we want to decrease the inventoryCount
	 */
	protected void decreaseInventoryCount(Equipment e) {
        if (inventoryCount.containsKey(e.toString())){
			int decrease = getInventoryCount(e)- 1;
			if (decrease == 0) {
			inventoryCount.remove(e.toString());
			} else {
				inventoryCount.put(e.toString(),decrease);
			}
		}
	}

	/** 
	 * Return the number of times this type of equipment occurs in the inventory.
	 * If it doesn't occur in the inventory, return -1 (to indicate that something went wrong somewhere).
	 * @param e
	 * @return
	 */
	public Integer getInventoryCount(Equipment e) {
		if (inventoryCount.get(e.toString()) != null){
			return inventoryCount.get(e.toString());
		}
        return -1;

	}
	/**
	 * Return the String representation of the EquipmentInventory.
	 * It should look similarly to the following:
	 * [EquipmentInventory: Guitar: 3, Stool: 3, Chair: 1, Keyboard: 2]
	 * (after adding 3 guitars, 3 stools, 1 chair and 2 keyboards).
	 * The order in which the types are printed does not matter.
	 * @return the string representation of the EquipmentInventory
	 */
	public String toString() {
		String out = "[EquipmentInventory:";
		for (Map.Entry<String, Integer> e : inventoryCount.entrySet()){
			out = out.concat(String.format(" %s: %d,",e.getKey(),e.getValue()));
		}
		out = (out.length() == 20) ? out : (out.substring(0,out.length()-1)).concat("]");
		return out;
	}

	public static void main(String[] args) {
		
		//ArrayList inventory = new ArrayList<Equipment>();
        EquipmentInventory equipmentinventory = new EquipmentInventory();
			Guitar guitar = new Guitar(); Guitar guitar1 = new Guitar(); Guitar guitar2 = new Guitar();
			Stool stool = new Stool(); Stool stool1 = new Stool(); Stool stool2 = new Stool();
			equipmentinventory.add(guitar); equipmentinventory.add(guitar1); equipmentinventory.add(guitar2);
			equipmentinventory.add(stool); equipmentinventory.add(stool1); equipmentinventory.add(stool2);
		Chair chair = new Chair();
		equipmentinventory.add(chair);
		Keyboard k1 = new Keyboard();
		Keyboard k2 = new Keyboard();
		equipmentinventory.add(k1);
		equipmentinventory.add(k2);
		System.out.println(equipmentinventory.toString());
		equipmentinventory.remove(k1);
		equipmentinventory.remove(stool);
		System.out.println(equipmentinventory.toString());
	}
}
