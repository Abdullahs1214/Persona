package OOP.lab2;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

public class BandNameGenerator {
	String[] adjectives;
	String[] nouns;

	boolean adjectivesLoaded = false;
	boolean nounsLoaded = false;

	String adjectivesFile;
	String nounsFile;

	public BandNameGenerator(String adjectivesFile, String nounsFile) {
		this.adjectivesFile = adjectivesFile;
		this.nounsFile = nounsFile;
	}

	/**
	 * Load the adjectives file and initialize that part of the generator.
	 */
	public void loadAdjectives() {
		adjectives = loadTxt(adjectivesFile);
		adjectivesLoaded = true;

	}

	/**
	 * Load the nouns file and initialize that part of the generator.
	 */
	public void loadNouns() {
		nouns = loadTxt(nounsFile);
		nounsLoaded = true;
	}

	/**
	 * Return a string that capitalizes only the first letter of s. So for example,
	 * cat becomes Cat.
	 * 
	 * @param s
	 * @return
	 */
	public String capitalizeFirst(String s) {
		String upperLetter = s.substring(0, 1).toUpperCase();
		String rest = s.substring(1);
		String uppercased = upperLetter + rest;
		return uppercased;
	}

	/**
	 * Generate a name for your band consisting of two adjectives and one noun. Make
	 * sure to return "UNINITIALIZED" if the band name generator is not initialized
	 * correctly yet.
	 * 
	 * @return the generated name or "UNINITIALIZED"
	 */
	public String generateName() {
		if (adjectivesLoaded == false || nounsLoaded == false) {
			return "UNINITIALIZED";
		} else {
			int lenAdjectives = adjectives.length;
			int lenNouns = nouns.length;
			int Number1 = (int) (Math.random() * lenAdjectives);
			int Number2 = (int) (Math.random() * lenAdjectives);
			int Number3 = (int) (Math.random() * lenNouns);
			return capitalizeFirst(adjectives[Number1]) + " " + capitalizeFirst(adjectives[Number2]) + " "
					+ capitalizeFirst(nouns[Number3]);
		}
	}

	/**
	 * This method loads a text file into a String array. It assumes the number of
	 * lines in the file is on the first line of the file itself.
	 * 
	 * Note: you are not allowed to make changes to this method. You can use this
	 * method for loading text files in the other lab and course assignments as
	 * well.
	 * 
	 * @param file
	 * @return
	 */
	private String[] loadTxt(String file) {
		String[] data = new String[0];
		BufferedReader in = null;

		try {
			in = new BufferedReader(new FileReader(file));
			String line;
			int i = 0;
			int totalLines = Integer.parseInt(in.readLine());
			data = new String[totalLines];
			while ((line = in.readLine()) != null) {
				data[i] = line;
				i++;

			}
		} catch (Exception e) {
			System.err.println("Problem while reading file: " + file);
			e.printStackTrace();
		} finally {
			if (in != null) {
				try {
					in.close();
				} catch (IOException e) {
					System.err.println("Problem closing file: " + file);
					e.printStackTrace();
				}
			}
		}
		return data;
	}

	/**
	 * Returns the list of adjectives.
	 * 
	 * @return
	 */
	public String[] getAdjectives() {
		return adjectives;
	}

	/**
	 * Returns the list of nouns.
	 * 
	 * @return
	 */
	public String[] getNouns() {
		return nouns;
	}

	public static void main(String[] args) {
		BandNameGenerator namegenerator = new BandNameGenerator("C:\\Users\\srskh\\Code files\\Java\\OOP\\lab2\\adjectives.txt", "C:\\Users\\srskh\\Code files\\Java\\OOP\\lab2\\nouns.txt");
		namegenerator.loadNouns();
		namegenerator.loadAdjectives();
		for (int i = 0; i < 20; i++) {
			System.out.println(namegenerator.generateName());
		}
		// create a BandNameGenerator and initialize it

		// generate and print 20 names for your band

	}

}