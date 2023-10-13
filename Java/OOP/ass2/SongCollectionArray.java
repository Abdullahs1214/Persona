package OOP.ass2;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

public class SongCollectionArray {
	private String[] songs;
	private int numsongs;
	
	/**
	 * Create a SongCollectionArray object with capacity i (= the number of songs it can hold).
	 * @param i the number of songs the collection can hold
	 */
	public SongCollectionArray(int i) {
		//size i object
		songs = new String[i];
		//empty array
		numsongs = 0;
	}
	
	
	/**
	 * Add s to the collection. Only add s if it is not in the collection yet. 
	 * Return true if the addition was successful, otherwise return false.
	 * 
	 * @param s the song to be added
	 * @return
	 */
	public boolean add(String s) {
		// false if array empty
		if (contains(s))
			return false; 
		// add element and number
		songs[numsongs++] = s;
		return true;
	}
	
	
	/**
	 * Remove s from the collection. Make sure that all the empty spots of the array 
	 * are at the end. So if you remove a song from the 'middle' of the array, you need to
	 * make sure that the empty spot is filled up somehow.
	 * @param s the song to be removed
	 */
	public void remove(String s) {
		//finding index of songs
		for (int i = 0; i < numsongs; i++) {
			//move to end of array
			if (songs[i].equals(s)) {
				songs[i] = songs[numsongs--];
				//delete end of array
				songs[numsongs + 1] = null;
				return;
			}
		}
	}
	
	/**
	 * Return true if the collection contains s, false otherwise.
	 * @param s the song to be searched for
	 * @return
	 */
	public boolean contains(String s) {		
		//check if song included
		for (String song : songs)
			if (s.equals(song))
				return true;
		return false;
	}
	
	/**
	 * If there is a song at position index in the collection, return it. Otherwise return null.
	 * @param index the index of the song to return
	 * @return
	 */
	public String getSong(int index) {
		//return index
		if (0 <= index && index < numsongs)
			return songs[index];
		
		return null;
	}
	
	/**
	 * Return the number of songs in the collection.
	 * @return
	 */
	public int getNumberOfSongs() {
		return numsongs;
	}
	
	/**
	 * Make sure to read the songs.txt file and print the number of unique songs in it.
	 * @param args
	 */
	public static void main(String[] args) {
		
		SongCollectionArray collection = new SongCollectionArray(100); 
		
		try (BufferedReader buffr = new BufferedReader(new FileReader("songs.txt"))) {
			
			int lines = Integer.valueOf(buffr.readLine());
			for (int i = 0; i++ < lines; collection.add(buffr.readLine()));
		} catch (IOException e) {
			e.printStackTrace();
		}
    
		System.out.println("Number of unique songs: " + collection.getNumberOfSongs());
	}
}