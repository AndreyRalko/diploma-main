from django.db import models


class Student(models.Model):
    id = models.AutoField(
        db_column="StudentID", primary_key=True
    )  # Field name made lowercase.
    firstname = models.CharField(max_length=128)
    lastname = models.CharField(max_length=128)
    patronymic = models.CharField(max_length=128, blank=True, null=True)

    startdate = models.DateField(
        db_column="StartDate", blank=True, null=True
    )  # Field name made lowercase.

    study_form = models.ForeignKey(
        db_column="StudyFormID",
        blank=True,
        null=True,
        to="Studyforms",
        on_delete=models.DO_NOTHING,
        db_constraint=False,
        related_name="study_form",
    )  # Field name made lowercase.
    profession = models.ForeignKey(
        db_column="ProfessionID",
        to="Professions",
        on_delete=models.DO_NOTHING,
        db_constraint=False,
        blank=True,
        null=True,
    )  # Field name made lowercase.
    coursenumber = models.IntegerField(
        db_column="CourseNumber", blank=True, null=True
    )  # Field name made lowercase.
    has_excellent = models.IntegerField(
        db_column="hasExcellent", blank=True, null=True
    )  # Field name made lowercase.
    is_student = models.IntegerField(
        db_column="isStudent", blank=True, null=True
    )  # Field name made lowercase.

    diploma_number = models.CharField(max_length=64, blank=True, null=True)

    specialization = models.ForeignKey(
        db_column="specializationID",
        to="Specializations",
        on_delete=models.DO_NOTHING,
        db_constraint=False,
        blank=True,
        null=True,
    )  # Field name made lowercase.

    iin = models.CharField(db_column="iinplt", max_length=32)

    firstname_en = models.CharField(max_length=128, blank=True, null=True)
    lastname_en = models.CharField(max_length=128, blank=True, null=True)
    patronymic_en = models.CharField(max_length=128, blank=True, null=True)

    class Meta:
        managed = False
        db_table = "students"


class Professions(models.Model):
    id = models.AutoField(
        db_column="professionID", primary_key=True
    )  # Field name made lowercase.
    name_ru = models.CharField(
        db_column="professionNameRU", max_length=128, blank=True, null=True
    )  # Field name made lowercase.
    name_kk = models.CharField(
        db_column="professionNameKZ", max_length=128, blank=True, null=True
    )  # Field name made lowercase.
    name_en = models.CharField(
        db_column="professionNameEN", max_length=128, blank=True, null=True
    )  # Field name made lowercase.
    professioncode = models.CharField(
        db_column="professionCode", max_length=128, blank=True, null=True
    )  # Field name made lowercase.
    created = models.DateField(blank=True, null=True)
    deleted = models.IntegerField(blank=True, null=True)
    code = models.CharField(max_length=8, blank=True, null=True)

    class Meta:
        managed = False
        db_table = "professions"


class Cafedras(models.Model):
    cafedraid = models.AutoField(
        db_column="cafedraID", primary_key=True
    )  # Field name made lowercase.
    cafedranameru = models.CharField(
        db_column="cafedraNameRU", max_length=128, blank=True, null=True
    )  # Field name made lowercase.
    cafedranamekz = models.CharField(
        db_column="cafedraNameKZ", max_length=128, blank=True, null=True
    )  # Field name made lowercase.
    cafedranameen = models.CharField(
        db_column="cafedraNameEN", max_length=128, blank=True, null=True
    )  # Field name made lowercase.
    facultyid = models.IntegerField(
        db_column="FacultyID", blank=True, null=True
    )  # Field name made lowercase.
    created = models.DateField(blank=True, null=True)
    cafedramanager = models.IntegerField(
        db_column="cafedraManager", blank=True, null=True
    )  # Field name made lowercase.
    informationru = models.TextField(
        db_column="informationRU", blank=True, null=True
    )  # Field name made lowercase.
    informationen = models.TextField(
        db_column="informationEN", blank=True, null=True
    )  # Field name made lowercase.
    informationkz = models.TextField(
        db_column="informationKZ", blank=True, null=True
    )  # Field name made lowercase.
    buildingid = models.IntegerField(
        db_column="buildingId", blank=True, null=True
    )  # Field name made lowercase.
    auditoryid = models.IntegerField(
        db_column="auditoryId", blank=True, null=True
    )  # Field name made lowercase.
    modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = "cafedras"


class ProfessionCafedra(models.Model):
    professionid = models.ForeignKey(
        "Professions",
        models.DO_NOTHING,
        db_column="professionID",
        blank=True,
        null=True,
    )  # Field name made lowercase.
    cafedraid = models.ForeignKey(
        Cafedras, models.DO_NOTHING, db_column="cafedraID", blank=True, null=True
    )  # Field name made lowercase.
    created = models.DateTimeField(blank=True, null=True)
    modified = models.DateTimeField()
    deleted = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "profession_cafedra"


class Specializations(models.Model):
    prof_caf = models.ForeignKey(
        ProfessionCafedra, models.DO_NOTHING, blank=True, null=True
    )
    name_ru = models.CharField(
        db_column="nameru", max_length=256, blank=True, null=True
    )
    name_kk = models.CharField(
        db_column="namekz", max_length=256, blank=True, null=True
    )
    name_en = models.CharField(
        db_column="nameen", max_length=256, blank=True, null=True
    )
    is_default = models.IntegerField(blank=True, null=True)
    created = models.DateTimeField(blank=True, null=True)
    modified = models.DateTimeField()
    deleted = models.DateTimeField(blank=True, null=True)
    code = models.CharField(
        db_column="specializationCode", max_length=16, blank=True, null=True
    )  # Field name made lowercase.
    is_narrow = models.IntegerField(blank=True, null=True)
    iseducationprogram = models.IntegerField(
        db_column="isEducationProgram", blank=True, null=True
    )  # Field name made lowercase.
    descriptionru = models.CharField(
        db_column="descriptionRU", max_length=256, blank=True, null=True
    )  # Field name made lowercase.
    descriptionkz = models.CharField(
        db_column="descriptionKZ", max_length=256, blank=True, null=True
    )  # Field name made lowercase.
    descriptionen = models.CharField(
        db_column="descriptionEN", max_length=256, blank=True, null=True
    )  # Field name made lowercase.
    eduprogtype = models.IntegerField(
        db_column="eduProgType", blank=True, null=True
    )  # Field name made lowercase.
    doublediploma = models.IntegerField(blank=True, null=True)
    jointep = models.IntegerField(
        db_column="jointEP", blank=True, null=True
    )  # Field name made lowercase.
    partnername = models.CharField(max_length=128, blank=True, null=True)
    ddstart = models.DateField(blank=True, null=True)
    statusep = models.IntegerField(
        db_column="statusEP", blank=True, null=True
    )  # Field name made lowercase.
    universitytype = models.IntegerField(
        db_column="universityType", blank=True, null=True
    )  # Field name made lowercase.
    partneruniverid = models.IntegerField(
        db_column="partnerUniverID", blank=True, null=True
    )  # Field name made lowercase.
    qualification_ru = models.CharField(max_length=1024, blank=True, null=True)
    qualification_kz = models.CharField(max_length=1024, blank=True, null=True)
    qualification_en = models.CharField(max_length=1024, blank=True, null=True)
    degree_ru = models.CharField(max_length=1024, blank=True, null=True)
    degree_kz = models.CharField(max_length=1024, blank=True, null=True)
    degree_en = models.CharField(max_length=1024, blank=True, null=True)
    is_interdisciplinary = models.IntegerField(blank=True, null=True)
    accessrequirementsru = models.TextField(
        db_column="accessRequirementsRU", blank=True, null=True
    )  # Field name made lowercase.
    accessrequirementskz = models.TextField(
        db_column="accessRequirementsKZ", blank=True, null=True
    )  # Field name made lowercase.
    accessrequirementsen = models.TextField(
        db_column="accessRequirementsEN", blank=True, null=True
    )  # Field name made lowercase.
    mainfieldofstudyforthequalificationru = models.TextField(
        db_column="mainFieldOfStudyForTheQualificationRU", blank=True, null=True
    )  # Field name made lowercase.
    mainfieldofstudyforthequalificationkz = models.TextField(
        db_column="mainFieldOfStudyForTheQualificationKZ", blank=True, null=True
    )  # Field name made lowercase.
    mainfieldofstudyforthequalificationen = models.TextField(
        db_column="mainFieldOfStudyForTheQualificationEN", blank=True, null=True
    )  # Field name made lowercase.
    keylearningoutcomesru = models.TextField(
        db_column="keyLearningOutcomesRU", blank=True, null=True
    )  # Field name made lowercase.
    keylearningoutcomeskz = models.TextField(
        db_column="keyLearningOutcomesKZ", blank=True, null=True
    )  # Field name made lowercase.
    keylearningoutcomesen = models.TextField(
        db_column="keyLearningOutcomesEN", blank=True, null=True
    )  # Field name made lowercase.
    accesstofurtherstudyru = models.TextField(
        db_column="accessToFurtherStudyRU", blank=True, null=True
    )  # Field name made lowercase.
    accesstofurtherstudykz = models.TextField(
        db_column="accessToFurtherStudyKZ", blank=True, null=True
    )  # Field name made lowercase.
    accesstofurtherstudyen = models.TextField(
        db_column="accessToFurtherStudyEN", blank=True, null=True
    )  # Field name made lowercase.
    overallclassificationqualificationru = models.TextField(
        db_column="overallClassificationQualificationRU", blank=True, null=True
    )  # Field name made lowercase.
    overallclassificationqualificationkz = models.TextField(
        db_column="overallClassificationQualificationKZ", blank=True, null=True
    )  # Field name made lowercase.
    overallclassificationqualificationen = models.TextField(
        db_column="overallClassificationQualificationEN", blank=True, null=True
    )  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = "specializations"


class Studentdiplomainfo(models.Model):
    studentid = models.IntegerField(
        db_column="studentID", primary_key=True
    )  # Field name made lowercase.
    protocol_number = models.CharField(
        db_column="minutesNumber", max_length=32, blank=True, null=True
    )  # Field name made lowercase.
    protocol_date = models.DateField(
        db_column="dateOfMinutes", blank=True, null=True
    )  # Field name made lowercase.
    diplomnumber = models.CharField(
        db_column="diplomNumber", max_length=32, blank=True, null=True
    )  # Field name made lowercase.
    dateofissue = models.DateField(
        db_column="dateOfIssue", blank=True, null=True
    )  # Field name made lowercase.
    registrationnumber = models.CharField(
        db_column="registrationNumber", max_length=32, blank=True, null=True
    )  # Field name made lowercase.
    dativefiokz = models.CharField(
        db_column="dativeFIOkz", max_length=128, blank=True, null=True
    )  # Field name made lowercase.
    dativefioru = models.CharField(
        db_column="dativeFIOru", max_length=128, blank=True, null=True
    )  # Field name made lowercase.
    dativefioen = models.CharField(
        db_column="dativeFIOen", max_length=128, blank=True, null=True
    )  # Field name made lowercase.
    year = models.IntegerField(blank=True, null=True)
    diplom_duplicate_given = models.IntegerField(blank=True, null=True)
    state_commission_decision_date = models.DateField(blank=True, null=True)
    certificate_series = models.CharField(max_length=32, blank=True, null=True)
    certificate_number = models.CharField(max_length=32, blank=True, null=True)
    certificate_registration_number = models.IntegerField(blank=True, null=True)
    certificate_issue_date = models.DateField(blank=True, null=True)
    iacdiplomaseries = models.CharField(
        db_column="iacDiplomaSeries", max_length=256, blank=True, null=True
    )  # Field name made lowercase.
    iacdiplomanumber = models.CharField(
        db_column="iacDiplomaNumber", max_length=256, blank=True, null=True
    )  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = "studentdiplomainfo"


class BaseEducation(models.Model):
    namekz = models.CharField(max_length=64, blank=True, null=True)
    nameru = models.CharField(max_length=64, blank=True, null=True)
    nameen = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        managed = False
        db_table = "base_education"


class Studyforms(models.Model):
    id = models.AutoField(
        db_column="Id", primary_key=True
    )  # Field name made lowercase.
    name_ru = models.CharField(
        db_column="NameRu", max_length=128, blank=True, null=True
    )  # Field name made lowercase.
    name_kk = models.CharField(
        db_column="NameKz", max_length=128, blank=True, null=True
    )  # Field name made lowercase.
    name_en = models.CharField(
        db_column="NameEn", max_length=128, blank=True, null=True
    )  # Field name made lowercase.
    formschedule = models.IntegerField(blank=True, null=True)
    coursecount = models.IntegerField(
        db_column="courseCount", blank=True, null=True
    )  # Field name made lowercase.
    maxyearscount = models.IntegerField(
        db_column="maxYearsCount", blank=True, null=True
    )  # Field name made lowercase.
    creditscount = models.IntegerField(
        db_column="creditsCount", blank=True, null=True
    )  # Field name made lowercase.
    checkscount = models.IntegerField(
        db_column="checksCount", blank=True, null=True
    )  # Field name made lowercase.
    enaughgraduategpa = models.FloatField(
        db_column="enaughGraduateGPA", blank=True, null=True
    )  # Field name made lowercase.
    excellentgraduategpa = models.FloatField(
        db_column="excellentGraduateGPA", blank=True, null=True
    )  # Field name made lowercase.
    finalattenaughcredits = models.IntegerField(
        db_column="finalAttEnaughCredits", blank=True, null=True
    )  # Field name made lowercase.
    termscount = models.IntegerField(
        db_column="termsCount", blank=True, null=True
    )  # Field name made lowercase.
    editiupdayscount = models.IntegerField(
        db_column="editIUPDaysCount", blank=True, null=True
    )  # Field name made lowercase.
    degreeid = models.IntegerField(
        db_column="degreeID", blank=True, null=True
    )  # Field name made lowercase.
    departmentid = models.IntegerField(
        db_column="departmentID", blank=True, null=True
    )  # Field name made lowercase.
    current_part = models.FloatField(blank=True, null=True)
    ratings_part = models.FloatField(blank=True, null=True)
    exam_part = models.FloatField(blank=True, null=True)
    use_ratings = models.IntegerField(blank=True, null=True)
    count_all_ratings = models.IntegerField(blank=True, null=True)
    excdiplomanoretake = models.IntegerField(
        db_column="excDiplomaNoRetake", blank=True, null=True
    )  # Field name made lowercase.
    excdiplomanosatisfactorymark = models.IntegerField(
        db_column="excDiplomaNoSatisfactoryMark", blank=True, null=True
    )  # Field name made lowercase.
    excdiplomagosprojectexcellentmarks = models.IntegerField(
        db_column="excDiplomaGosProjectExcellentMarks", blank=True, null=True
    )  # Field name made lowercase.
    base_education = models.ForeignKey(
        BaseEducation, models.DO_NOTHING, blank=True, null=True
    )
    term_credits = models.FloatField(blank=True, null=True)
    summer_term_credits = models.FloatField(blank=True, null=True)
    change_percent = models.IntegerField(blank=True, null=True)
    average_weekly_load_hours = models.IntegerField(blank=True, null=True)
    practice_credits = models.IntegerField(blank=True, null=True)
    allow_with_nopass = models.IntegerField(blank=True, null=True)
    standard_study_education_month = models.IntegerField(blank=True, null=True)
    standard_study_education_year = models.IntegerField(blank=True, null=True)
    percentage_excellent = models.IntegerField(blank=True, null=True)
    onlineregprovided = models.IntegerField(
        db_column="onlineRegProvided", blank=True, null=True
    )  # Field name made lowercase.
    diploma_honor_provided = models.IntegerField(blank=True, null=True)
    block_journal = models.IntegerField(blank=True, null=True)
    trainingcompletionterm = models.IntegerField(
        db_column="trainingCompletionTerm", blank=True, null=True
    )  # Field name made lowercase.
    official_duration_of_the_program_ru = models.CharField(
        max_length=256, blank=True, null=True
    )
    official_duration_of_the_program_kz = models.CharField(
        max_length=256, blank=True, null=True
    )
    official_duration_of_the_program_en = models.CharField(
        max_length=256, blank=True, null=True
    )
    is_sufficient_gpa_for_course = models.IntegerField(blank=True, null=True)
    is_transcript_unsatisfactory_marks_absent = models.IntegerField(
        blank=True, null=True
    )
    is_overall_average_gpa_sufficient = models.IntegerField(blank=True, null=True)
    overall_average_gpa = models.FloatField(blank=True, null=True)
    is_assimilated_credits_sufficient = models.IntegerField(blank=True, null=True)
    termofsubjectsineuropeandiploma = models.IntegerField(
        db_column="termOfSubjectsInEuropeanDiploma", blank=True, null=True
    )  # Field name made lowercase.
    distance_learning = models.IntegerField(blank=True, null=True)
    exc_diploma_take_into_account_theoretical_gos_disciplines = models.IntegerField(
        blank=True, null=True
    )
    payment_debts = models.CharField(max_length=128, blank=True, null=True)
    providedremovecontrols = models.IntegerField(
        db_column="providedRemoveControls", blank=True, null=True
    )  # Field name made lowercase.
    modified = models.DateTimeField()
    marktypes = models.CharField(
        db_column="markTypes", max_length=128, blank=True, null=True
    )  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = "studyforms"


class DegreeTypes(models.Model):
    degreeid = models.AutoField(
        db_column="degreeID", primary_key=True
    )  # Field name made lowercase.
    name_ru = models.CharField(max_length=256, blank=True, null=True)
    name_kk = models.CharField(
        db_column="name_kz", max_length=256, blank=True, null=True
    )
    name_en = models.CharField(max_length=256, blank=True, null=True)
    degree_ru = models.CharField(max_length=256, blank=True, null=True)
    degree_kk = models.CharField(
        db_column="degree_kz", max_length=256, blank=True, null=True
    )
    degree_en = models.CharField(max_length=256, blank=True, null=True)

    class Meta:
        managed = False
        db_table = "degree_types"
