from s1_video_learningVideo.ss import data_import as di
from s1_video_learningVideo.store import data_export as de
# import s1_video_learningVideo.ss.data_import as di

def to_stage():
    di.main()
    
def to_dwh():
    de.main()

def main():
    pass

if __name__ == "__main__":
    main()