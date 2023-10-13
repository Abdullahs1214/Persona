package OOP.ass2;

import java.io.BufferedReader;

import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;

public class SongCollectionArrayList {
	private ArrayList<String> songs;

	/**
	 * Create a SongCollectionArrayList object.
	 * 
	 */
	public SongCollectionArrayList() {
		songs = new ArrayList<String>();
	}

	/**
	 * Add s to the collection. Only add s if it is not in the collection yet. 
	 * Return true if the addition was successful, otherwise return false.
	 * 
	 * @param s the song to be added
	 * @return
	 */
	public boolean add(String s) {
		if (songs.contains(s)){
			return false;
		}
		songs.add(s);
		return true;
		}
	

	/**
	 * Remove s from the collection.
	 * @param s the song to be removed
	 */
	public void remove(String s) {
		songs.remove(s);
	}

	/**
	 * Return true if the collection contains s, false otherwise.
	 * @param s the song to be searched for
	 * @return
	 */
	public boolean contains(String s) {
		return songs.contains(s);
	}
	
	/**
	 * If there is a song at position index in the collection, return it. Otherwise return null.
	 * @param index the index of the song to return
	 * @return
	 */
	public String getSong(int index) {
		if ( 0 <= index && index < songs.size()){
			if (songs.get(index) != ""){
				return songs.get(index);
			}
		}
			return null;
	}


	/**
	 * Return the number of songs in the collection.
	 * @return
	 */
	public int getNumberOfSongs() {
		return songs.size();
	}
	
	/**
	 * Make sure to read the songs.txt file and print the number of unique songs in it.
	 * @param args
	 */
	public static void main(String[] args) {
		SongCollectionArray collection = new SongCollectionArray(100); 
		try (BufferedReader buffr = new BufferedReader(new FileReader("C:\\Users\\srskh\\Code files\\Java\\OOP\\ass2\\songs.txt"))) {
			int lines = Integer.valueOf(buffr.readLine());
			for (int i = 0; i++ < lines; collection.add(buffr.readLine()));
		} catch (IOException e) {
			e.printStackTrace();
		}
    
		System.out.println("Number of unique songs: " + collection.getNumberOfSongs());
	}
	}


