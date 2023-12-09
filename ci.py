import subprocess
import glob

def run_all_python_files(files):

    for file in files:
        print("Running", file)
        exit_code = run_python_script(file)
        if exit_code != 0:
            print(f"Error in {file}. Exiting with status code {exit_code}.")
            return exit_code
    return 0


def run_python_script(file_path):
    try:
        subprocess.check_output(["python3", file_path], stderr=subprocess.STDOUT, universal_newlines=True)
        return 0
    except subprocess.CalledProcessError as e:
        print(f"Exception in {file_path}: {e.output}")
        return e.returncode


if __name__ == "__main__":

    # Utilisez le motif '*.py' pour rechercher tous les fichiers se terminant par '.py'
    python_files = glob.glob('day_*/*.py')

    # Affichez la liste des fichiers trouvés
    print("Fichiers Python trouvés :")
    for file in python_files:
        print(file)
    exit_code = run_all_python_files(python_files)
    print(f"Exiting with status code {exit_code}.")
    exit(exit_code)
