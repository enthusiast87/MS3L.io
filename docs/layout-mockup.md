export default function MS3LHomepageMockup() {
  const navItems = [
    "Home",
    "Introduction",
    "Members",
    "Projects",
    "Publications",
    "Patents",
    "News",
    "Contacts",
  ];

  const researchThemes = [
    {
      title: "Biorefinery",
      description:
        "Membrane-enabled product recovery, catalyst recycling, and sustainable downstream processing.",
    },
    {
      title: "Plastic Recycling",
      description:
        "Selective purification, solvent recovery, and circular separation processes for recycled feedstocks.",
    },
    {
      title: "Resource Recovery",
      description:
        "Membrane distillation, crystallization, and purification technologies for valuable resource recovery.",
    },
    {
      title: "Energy Applications",
      description:
        "Separation technologies for biofuels, pressure retarded osmosis, and battery-related systems.",
    },
  ];

  const publications = [
    "Membrane-based sustainable separation for biorefinery systems",
    "Selective purification strategies for circular plastic recycling",
    "Advanced membrane processes for resource recovery and solvent recycling",
  ];

  const news = [
    "Lab website migration to GitHub Pages in progress",
    "Research themes and member pages will be updated gradually",
    "Selected publications and patents section under refinement",
  ];

  return (
    <div className="min-h-screen bg-slate-50 text-slate-800">
      <header className="sticky top-0 z-20 border-b border-slate-200 bg-white/90 backdrop-blur">
        <div className="mx-auto flex max-w-6xl items-center justify-between px-6 py-4">
          <div>
            <div className="text-xl font-semibold tracking-tight">MS³L</div>
            <div className="text-sm text-slate-500">
              Membrane-based Sustainable Separation Solutions Laboratory
            </div>
          </div>
          <nav className="hidden gap-6 text-sm md:flex">
            {navItems.map((item) => (
              <a key={item} href="#" className="transition hover:text-slate-950 text-slate-600">
                {item}
              </a>
            ))}
          </nav>
        </div>
      </header>

      <main>
        <section className="border-b border-slate-200 bg-white">
          <div className="mx-auto grid max-w-6xl gap-10 px-6 py-16 md:grid-cols-[1.5fr,1fr] md:py-24">
            <div className="space-y-6">
              <div className="inline-flex rounded-full border border-slate-300 px-3 py-1 text-xs font-medium uppercase tracking-[0.2em] text-slate-500">
                Academic Lab Website Draft
              </div>
              <div className="space-y-4">
                <h1 className="max-w-3xl text-4xl font-semibold leading-tight tracking-tight md:text-5xl">
                  Sustainable membrane separation solutions for resource circulation, energy, and biorefinery systems.
                </h1>
                <p className="max-w-2xl text-base leading-7 text-slate-600 md:text-lg">
                  This layout draft keeps the overall clarity of your current Google Sites page,
                  while making the structure more professional and easier to expand later with
                  publications, patents, members, and automated updates.
                </p>
              </div>
              <div className="flex flex-wrap gap-3">
                <button className="rounded-2xl bg-slate-900 px-5 py-3 text-sm font-medium text-white shadow-sm transition hover:opacity-90">
                  View Research Themes
                </button>
                <button className="rounded-2xl border border-slate-300 bg-white px-5 py-3 text-sm font-medium text-slate-700 transition hover:bg-slate-100">
                  Meet the Lab
                </button>
              </div>
            </div>

            <div className="rounded-3xl border border-slate-200 bg-slate-100 p-6 shadow-sm">
              <div className="mb-4 text-sm font-semibold uppercase tracking-wide text-slate-500">
                PI / Lab Overview
              </div>
              <div className="space-y-4">
                <div className="h-40 rounded-2xl bg-white shadow-inner" />
                <div>
                  <div className="text-lg font-semibold">Jihoon Kim</div>
                  <div className="text-sm text-slate-500">Principal Investigator</div>
                </div>
                <p className="text-sm leading-6 text-slate-600">
                  Research focus on membrane-based sustainable separations for biorefinery,
                  plastic recycling, resource recovery, and energy-related applications.
                </p>
              </div>
            </div>
          </div>
        </section>

        <section className="mx-auto max-w-6xl px-6 py-16">
          <div className="mb-8 flex items-end justify-between gap-4">
            <div>
              <div className="text-sm font-semibold uppercase tracking-[0.2em] text-slate-500">
                Research Themes
              </div>
              <h2 className="mt-2 text-3xl font-semibold tracking-tight">Core research areas</h2>
            </div>
            <div className="hidden text-sm text-slate-500 md:block">
              Structured cards for a cleaner first impression
            </div>
          </div>

          <div className="grid gap-5 md:grid-cols-2 xl:grid-cols-4">
            {researchThemes.map((theme) => (
              <div
                key={theme.title}
                className="rounded-3xl border border-slate-200 bg-white p-6 shadow-sm transition hover:-translate-y-0.5 hover:shadow-md"
              >
                <h3 className="text-lg font-semibold">{theme.title}</h3>
                <p className="mt-3 text-sm leading-6 text-slate-600">{theme.description}</p>
              </div>
            ))}
          </div>
        </section>

        <section className="border-y border-slate-200 bg-white">
          <div className="mx-auto grid max-w-6xl gap-10 px-6 py-16 md:grid-cols-[1.2fr,0.8fr]">
            <div>
              <div className="text-sm font-semibold uppercase tracking-[0.2em] text-slate-500">
                Selected Publications
              </div>
              <h2 className="mt-2 text-3xl font-semibold tracking-tight">
                Representative work
              </h2>
              <div className="mt-8 space-y-4">
                {publications.map((item, idx) => (
                  <div key={idx} className="rounded-2xl border border-slate-200 bg-slate-50 p-5">
                    <div className="text-sm font-medium text-slate-400">0{idx + 1}</div>
                    <div className="mt-2 text-base font-medium leading-7 text-slate-800">{item}</div>
                  </div>
                ))}
              </div>
            </div>

            <div>
              <div className="text-sm font-semibold uppercase tracking-[0.2em] text-slate-500">
                Latest News
              </div>
              <h2 className="mt-2 text-3xl font-semibold tracking-tight">Recent updates</h2>
              <div className="mt-8 space-y-4">
                {news.map((item, idx) => (
                  <div key={idx} className="rounded-2xl border border-slate-200 bg-slate-50 p-5">
                    <div className="text-sm text-slate-400">March 2026</div>
                    <div className="mt-2 text-sm leading-6 text-slate-700">{item}</div>
                  </div>
                ))}
              </div>
            </div>
          </div>
        </section>

        <section className="mx-auto max-w-6xl px-6 py-16">
          <div className="grid gap-6 md:grid-cols-3">
            <div className="rounded-3xl border border-slate-200 bg-white p-6 shadow-sm">
              <div className="text-sm font-semibold uppercase tracking-[0.2em] text-slate-500">
                Members
              </div>
              <h3 className="mt-3 text-xl font-semibold">People</h3>
              <p className="mt-3 text-sm leading-6 text-slate-600">
                Faculty, graduate students, and collaborators presented in a compact academic layout.
              </p>
            </div>
            <div className="rounded-3xl border border-slate-200 bg-white p-6 shadow-sm">
              <div className="text-sm font-semibold uppercase tracking-[0.2em] text-slate-500">
                Patents & Projects
              </div>
              <h3 className="mt-3 text-xl font-semibold">Outputs</h3>
              <p className="mt-3 text-sm leading-6 text-slate-600">
                Space for technology transfer, patents, sponsored projects, and major milestones.
              </p>
            </div>
            <div className="rounded-3xl border border-slate-200 bg-white p-6 shadow-sm">
              <div className="text-sm font-semibold uppercase tracking-[0.2em] text-slate-500">
                Contact
              </div>
              <h3 className="mt-3 text-xl font-semibold">Get in touch</h3>
              <p className="mt-3 text-sm leading-6 text-slate-600">
                Office location, email, and recruitment information can sit here in a clean footer block.
              </p>
            </div>
          </div>
        </section>
      </main>
    </div>
  );
}
