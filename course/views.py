from django.shortcuts import render
from django.utils import timezone
from .models import Chapter, SubChapter, SubSection
from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect

def chapter_list(request):
	chapters = Chapter.objects.all()
	return render(request, 'cefs/chapter_list.html', {'chapters':chapters})

def subchapter_list(request, pk):
	chapter = get_object_or_404(Chapter, pk=pk)
	subchapters = chapter.subchapter_set.all()
	return render(request, 'cefs/subchapter_list.html', {'subchapters':subchapters, 'chapter':chapter})

def subsection_list(request, pk, slug):
	sub_chapter = get_object_or_404(SubChapter, slug=slug)
	sub_sections = sub_chapter.subsection_set.all()
	subchapter = get_object_or_404(Chapter, pk=pk)
	return render(request, 'cefs/sub_section_list.html', {'sub_sections':sub_sections, 'subchapter':subchapter, 'sub_chapter':sub_chapter})

# edit this to determine how subsections are queried and published
def detail(request, pk, slug, slug2):
	course = get_object_or_404(SubSection, slug=slug2)
	subsection = get_object_or_404(SubChapter, slug=slug)
	return render(request, 'cefs/detail.html', {'course':course, 'subsection':subsection})
